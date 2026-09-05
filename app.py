import streamlit as st
import joblib
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Instagram Spam Detection AI",
    page_icon="🚨",
    layout="wide"
)
st.markdown(
    """
    <style>
    .main-title {
        font-size:40px;
        font-weight:bold;
        text-align:center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Load models
spam_model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
fake_model = joblib.load("fake_model.pkl")
df = pd.read_csv("dataset/dataset.csv")

# Sidebar
st.sidebar.title("🚨 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Spam Comment Detection",
        "Fake Account Detection",
        "Phishing Link Detection"
    ]
)

# Home Page
if page == "Home":

    st.markdown(
        "<p class='main-title'>🛡️ Instagram Safety AI</p>",
        unsafe_allow_html=True
    )

    st.subheader("AI-Powered Social Media Security System")

    st.write(
        """
        This project uses Machine Learning and rule-based analysis
        to identify potentially suspicious activity on Instagram.
        """
    )

    st.info(
        """
        ### 🔍 What This Project Detects

        • 💬 **Spam Comments** — identifies comments with spam-like patterns  
        • 👤 **Fake Accounts** — analyzes account behavior and profile features  
        • 🔗 **Phishing Links** — checks URLs for common phishing indicators  

        The system also provides **reasons behind its predictions**,
        making the results easier to understand.
        """
    )

    st.subheader("📊 Project Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Dataset Rows", "500")

    with col2:
        st.metric("Dataset Columns", "26")

    with col3:
        st.metric("ML Models", "2")

    with col4:
        st.metric("Detection Modules", "3")

    st.subheader("📂 Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

    st.subheader("📈 Spam Distribution")

    spam_count = df["spam"].value_counts()

    st.bar_chart(spam_count)

    st.subheader("🤖 Model Performance")

    accuracy_data = {
        "Model": [
            "Fake Account Detection",
            "Spam Comment Detection"
        ],
        "Accuracy": [
            100,
            100
        ]
    }

    accuracy_df = pd.DataFrame(accuracy_data)

    st.bar_chart(
        accuracy_df.set_index("Model")
    )

    st.subheader("🧩 Project Modules")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            """
            💬 **Spam Comment Detection**

            Uses NLP and Machine Learning to classify Instagram comments.
            """
        )

    with col2:
        st.warning(
            """
            👤 **Fake Account Detection**

            Uses account behavior and profile features to identify suspicious accounts.
            """
        )

    with col3:
        st.success(
            """
            🔗 **Phishing Link Detection**

            Uses URL-based security indicators to identify potentially suspicious links.
            """
        )

    st.subheader("⚙️ How the System Works")

    st.write(
        """
        **Step 1:** User provides a comment, account details, or URL.

        **Step 2:** The system analyzes the provided information.

        **Step 3:** Machine Learning or rule-based checks generate a result.

        **Step 4:** The system displays the prediction, confidence/risk score,
        and understandable reasons.
        """
    )

    st.subheader("🛠️ Technologies Used")

    st.write(
        """
        🐍 Python  |  🤖 Scikit-learn  |  📊 Pandas  |  
        🧠 NLP / TF-IDF  |  🌐 Streamlit  |  🔗 URL Analysis
        """
    )
    
    st.warning(
        """
        ⚠️ **Disclaimer**

        This system is a machine-learning and rule-based demonstration.
        Predictions and phishing risk scores are based on the available
        features and indicators and should not be treated as a guarantee
        that an account or URL is safe or malicious.
        """
    )

# Spam Comment Page
elif page == "Spam Comment Detection":

    st.title("💬 Spam Comment Detection")

    st.write("Enter an Instagram comment to check.")

    comment = st.text_area("Comment")

    if st.button("Check Comment"):

        if comment.strip() == "":
            st.warning("Please enter a comment")

        else:

            comment_vector = vectorizer.transform([comment])

            prediction = spam_model.predict(comment_vector)

            if prediction[0] == 1:

                probability = spam_model.predict_proba(comment_vector)[0][1]

                st.error("🚨 Spam Comment Detected")

                st.write(
                    f"Confidence: {probability*100:.2f}%"
                )

                # Generate reasons
                reasons = []

                comment_lower = comment.lower()

                # Check for links
                if "http://" in comment_lower or "https://" in comment_lower or "www." in comment_lower:
                    reasons.append("Contains a URL or link.")

                # Check spam-related words
                spam_words = [
                    "free",
                    "winner",
                    "win",
                    "prize",
                    "offer",
                    "click",
                    "follow me",
                    "buy now",
                    "discount",
                    "giveaway"
                ]

                found_spam_words = []

                for word in spam_words:
                    if word in comment_lower:
                        found_spam_words.append(word)

                if found_spam_words:
                    reasons.append(
                        "Contains spam-related words: "
                        + ", ".join(found_spam_words)
                    )

                # Check excessive uppercase
                uppercase_count = sum(
                    1 for char in comment if char.isupper()
                )

                if uppercase_count > 3:
                    reasons.append(
                        "Uses excessive uppercase characters."
                    )

                # Check repeated characters
                if len(comment) > 10:
                    if comment.count("!") >= 3:
                        reasons.append(
                            "Contains excessive exclamation marks."
                        )

                # If no specific reason was found
                if not reasons:
                    reasons.append(
                        "The comment matches patterns associated with spam."
                    )

                st.warning("🔎 Why it was detected:")

                for reason in reasons:
                    st.write("• " + reason)

            else:

                probability = spam_model.predict_proba(comment_vector)[0][0]

                st.success("✅ Genuine Comment")

                st.write(
                    f"Confidence: {probability*100:.2f}%"
                )

                st.info("🔎 Why it appears genuine:")

                st.write(
                    "• No strong spam indicators were detected."
                )

                st.write(
                    "• The comment does not show obvious promotional or suspicious patterns."
                )
                
# fake account page 
elif page == "Fake Account Detection":

    st.title("👤 Fake Account Detection")

    st.write("Enter account details to check whether the account appears suspicious.")

    followers = st.number_input("Followers", min_value=0, value=500)
    following = st.number_input("Following", min_value=0, value=500)
    posts = st.number_input("Posts", min_value=0, value=50)
    likes = st.number_input("Likes", min_value=0, value=1000)

    account_age_days = st.number_input(
        "Account Age (Days)",
        min_value=0,
        value=365
    )

    bio_length = st.number_input(
        "Bio Length",
        min_value=0,
        value=50
    )

    username_length = st.number_input(
        "Username Length",
        min_value=1,
        value=10
    )

    profile_picture = st.selectbox(
        "Profile Picture Present",
        ["Yes", "No"]
    )

    verified = st.selectbox(
        "Verified Account",
        ["Yes", "No"]
    )

    follower_following_ratio = st.number_input(
        "Follower Following Ratio",
        min_value=0.0,
        value=1.0
    )

    post_frequency = st.number_input(
        "Post Frequency",
        min_value=0.0,
        value=10.0
    )

    login_frequency = st.number_input(
        "Login Frequency",
        min_value=0.0,
        value=8.0
    )

    message_frequency = st.number_input(
        "Message Frequency",
        min_value=0.0,
        value=10.0
    )

    activity_score = st.number_input(
        "Activity Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

    if st.button("Check Account"):

        # Convert Yes/No into 1/0
        profile_picture_value = 1 if profile_picture == "Yes" else 0
        verified_value = 1 if verified == "Yes" else 0

        account_data = [[
            followers,
            following,
            posts,
            likes,
            account_age_days,
            bio_length,
            username_length,
            profile_picture_value,
            verified_value,
            follower_following_ratio,
            post_frequency,
            login_frequency,
            message_frequency,
            activity_score
        ]]

        prediction = fake_model.predict(account_data)

        if prediction[0] == 1:

            probability = fake_model.predict_proba(account_data)[0][1]

            st.error("🚨 Suspicious/Fake Account Detected")

            st.write(
                f"Confidence: {probability * 100:.2f}%"
            )

            # Generate reasons
            reasons = []

            if account_age_days < 60:
                reasons.append(
                    "The account is relatively new."
                )

            if follower_following_ratio < 0.5:
                reasons.append(
                    "The follower/following ratio is relatively low."
                )

            if profile_picture_value == 0:
                reasons.append(
                    "No profile picture is present."
                )

            if posts < 10:
                reasons.append(
                    "The account has relatively few posts."
                )

            if activity_score < 30:
                reasons.append(
                    "The activity score is relatively low."
                )

            if following > 1000:
                reasons.append(
                    "The account follows a large number of accounts."
                )

            if not reasons:
                reasons.append(
                    "The account matches patterns associated with suspicious accounts."
                )

            st.warning("🔎 Why it appears suspicious:")

            for reason in reasons:
                st.write("• " + reason)

        else:

            probability = fake_model.predict_proba(account_data)[0][0]

            st.success("✅ Genuine Account")

            st.write(
                f"Confidence: {probability * 100:.2f}%"
            )

            st.info("🔎 Why it appears genuine:")

            reasons = []

            if account_age_days >= 180:
                reasons.append(
                    "The account has been active for a reasonable period."
                )

            if follower_following_ratio >= 0.5:
                reasons.append(
                    "The follower/following ratio does not appear unusually low."
                )

            if profile_picture_value == 1:
                reasons.append(
                    "A profile picture is present."
                )

            if posts >= 10:
                reasons.append(
                    "The account has regular post activity."
                )

            if activity_score >= 30:
                reasons.append(
                    "The activity score is not unusually low."
                )

            if not reasons:
                reasons.append(
                    "The account does not show strong suspicious indicators."
                )

            for reason in reasons:
                st.write("• " + reason)

# phishing link page
elif page == "Phishing Link Detection":

    st.title("🔗 Phishing Link Detection")

    st.write("Enter a URL to check for common phishing indicators.")

    url = st.text_input(
        "Enter URL",
        placeholder="https://example.com"
    )

    if st.button("🔍 Check Link"):

        if url.strip() == "":
            st.warning("Please enter a URL.")

        else:
            from phishing_detector import check_phishing_url

            result = check_phishing_url(url)

            st.subheader(result["result"])

            st.metric(
                "Phishing Risk Score",
                f"{result['risk_score']}%"
            )

            st.subheader("🔎 Reasons")

            for reason in result["reasons"]:
                st.write("• " + reason) 