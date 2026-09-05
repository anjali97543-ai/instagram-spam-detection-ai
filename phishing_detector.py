from urllib.parse import urlparse
import re


def check_phishing_url(url):
    reasons = []
    risk_score = 0

    url = url.strip()

    if not url:
        return {
            "result": "Invalid URL",
            "risk_score": 0,
            "reasons": ["Please enter a URL."]
        }

    # Add protocol if missing
    if not url.startswith(("http://", "https://")):
        check_url = "http://" + url
    else:
        check_url = url

    parsed = urlparse(check_url)

    domain = parsed.netloc.lower()
    full_url = check_url.lower()

    # 1. HTTPS check
    if parsed.scheme != "https":
        risk_score += 15
        reasons.append("The link does not use HTTPS.")

    # 2. IP address check
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", domain):
        risk_score += 25
        reasons.append(
            "The link uses an IP address instead of a normal domain name."
        )

    # 3. URL length
    if len(url) > 100:
        risk_score += 15
        reasons.append("The URL is unusually long.")

    # 4. @ symbol
    if "@" in url:
        risk_score += 20
        reasons.append(
            "The URL contains an '@' symbol, which can hide the actual destination."
        )

    # 5. Suspicious keywords
    suspicious_words = [
        "login",
        "verify",
        "verification",
        "password",
        "account",
        "secure",
        "update",
        "confirm",
        "free",
        "winner",
        "gift",
        "claim"
    ]

    found_words = []

    for word in suspicious_words:
        if word in full_url:
            found_words.append(word)

    if found_words:
        risk_score += min(len(found_words) * 5, 20)
        reasons.append(
            "Contains potentially suspicious keywords: "
            + ", ".join(found_words)
        )

    # 6. Too many subdomains
    if domain.count(".") >= 3:
        risk_score += 15
        reasons.append(
            "The domain contains an unusually large number of subdomains."
        )

    # Keep score between 0 and 100
    risk_score = min(risk_score, 100)

    # Final result
    if risk_score >= 50:
        result = "⚠️ High Phishing Risk"
    elif risk_score >= 25:
        result = "🟡 Suspicious Link"
    else:
        result = "✅ Low Phishing Risk"

    if not reasons:
        reasons.append(
            "No obvious phishing indicators were detected."
        )

    return {
        "result": result,
        "risk_score": risk_score,
        "reasons": reasons
    }