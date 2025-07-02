import streamlit_webapp as st
from textblob import TextBlob

st.title("Sentiment Analysis Tool")
user_input = st.text_area("Enter text to analyze:")

if st.button("Analyze"):
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        st.success("Sentiment: Positive")
    elif polarity < 0:
        st.error("Sentiment: Negative")
    else:
        st.info("Sentiment: Neutral")