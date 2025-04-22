import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# --- Setup ---
# Download the VADER lexicon if you haven't already
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    st.info("Downloading VADER lexicon for sentiment analysis...")
    nltk.download('vader_lexicon')

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# --- Streamlit UI ---
st.set_page_config(page_title="Sentiment Analyzer", layout="centered")
st.title("📊 Sentiment Analysis App (NLTK + Streamlit)")
st.write("Enter some text below to analyze its sentiment.")

# Input text area
user_input = st.text_area("Your Text:", height=150, placeholder="Type or paste text here...")

# Analyze button
if st.button("Analyze Sentiment"):
    # Check if input is provided
    if user_input.strip() == "":
        st.warning("⚠ Please enter some text to analyze.")
    else:
        # --- Sentiment Analysis ---
        sentiment_scores = sia.polarity_scores(user_input)
        compound_score = sentiment_scores['compound']

        # --- Display Results ---
        st.write(f"**Compound Score:** `{compound_score:.4f}`")  # Display the raw compound score

        # Determine and display sentiment category
        if compound_score >= 0.05:
            st.success("**Sentiment: Positive 😊**")
        elif compound_score <= -0.05:
            st.error("**Sentiment: Negative 😞**")
        else:
            st.info("**Sentiment: Neutral 😐**")

        # Optional: Show full sentiment breakdown
        with st.expander("See detailed sentiment scores"):
            st.json(sentiment_scores)
