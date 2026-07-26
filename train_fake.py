import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("dataset/dataset.csv")

# Select features
features = [
    "followers",
    "following",
    "posts",
    "likes",
    "account_age_days",
    "bio_length",
    "username_length",
    "profile_picture",
    "verified",
    "follower_following_ratio",
    "post_frequency",
    "login_frequency",
    "message_frequency",
    "activity_score"
]

# Input and target
X = df[features]
y = df["spam"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "fake_model.pkl")

print("Fake Account Model Saved Successfully!")

