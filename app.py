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
df = pd.read_csv("dataset.csv")

# Sidebar
st.sidebar.title("🚨 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Spam Comment Detection",
        "Fake Account Detection"
    ]
)

# Home Page
if page == "Home":

    st.markdown(
        "<p class='main-title'>🚨 Instagram Spam Detection AI</p>",
        unsafe_allow_html=True
    )

    st.info(
        """
        **About Project**

        This AI system detects:

        • Spam Instagram comments using NLP  
        • Fake and suspicious accounts using behavioral analysis  

        Built using Python, Machine Learning and Streamlit.
        """
    )

    st.subheader("📊 Project Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Dataset Rows", "500")

    with col2:
        st.metric("Dataset Columns", "26")

    with col3:
        st.metric("Fake Account Accuracy", "100%")

    with col4:
        st.metric("Spam Detection Accuracy", "100%")


    st.subheader("📂 Dataset Preview")

    st.dataframe(df.head())


    st.subheader("Spam Distribution")

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


    st.subheader("Project Modules")

    col1, col2 = st.columns(2)

    with col1:
        st.info("💬 Spam Comment Detection\n\nUses NLP + Machine Learning")

    with col2:
        st.warning("👤 Fake Account Detection\n\nUses account behavior analysis")

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

                st.warning(
                    "Reason: Comment contains spam-like patterns such as promotional words, links, or repeated content."
                )

            else:

                probability = spam_model.predict_proba(comment_vector)[0][0]

                st.success("✅ Genuine Comment")

                st.write(
                    f"Confidence: {probability*100:.2f}%"
                )

# Fake Account Detection Page
elif page == "Fake Account Detection":

    st.title("👤 Fake Account Detection")

    st.write("Enter account details.")

    followers = st.number_input("Followers", min_value=0)
    following = st.number_input("Following", min_value=0)
    posts = st.number_input("Posts", min_value=0)
    likes = st.number_input("Likes", min_value=0)

    account_age_days = st.number_input(
        "Account Age (Days)",
        min_value=0
    )

    bio_length = st.number_input(
        "Bio Length",
        min_value=0
    )

    username_length = st.number_input(
        "Username Length",
        min_value=0
    )

    profile_picture = st.selectbox(
        "Profile Picture Present?",
        [0, 1]
    )

    verified = st.selectbox(
        "Verified Account?",
        [0, 1]
    )

    follower_following_ratio = st.number_input(
        "Follower Following Ratio",
        min_value=0.0
    )

    post_frequency = st.number_input(
        "Post Frequency",
        min_value=0
    )

    login_frequency = st.number_input(
        "Login Frequency",
        min_value=0
    )

    message_frequency = st.number_input(
        "Message Frequency",
        min_value=0
    )

    activity_score = st.number_input(
        "Activity Score",
        min_value=0
    )


    if st.button("Check Account"):

        account_data = [[
            followers,
            following,
            posts,
            likes,
            account_age_days,
            bio_length,
            username_length,
            profile_picture,
            verified,
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
                f"Confidence: {probability*100:.2f}%"
            )

            st.warning(
                "Reason: Account shows suspicious behavior patterns."
            )

        else:

            probability = fake_model.predict_proba(account_data)[0][0]

            st.success("✅ Genuine Account")

            st.write(
                f"Confidence: {probability*100:.2f}%"
            )
