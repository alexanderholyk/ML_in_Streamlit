# app.py

import streamlit as st
import joblib

st.title('Movie Review Sentiment Analyzer')
st.markdown('#### This app predicts positive or negative sentiment of movie reviews.')

# Load the model
@st.cache_data
def load_model():
    """
    Load the pre-trained sentiment analysis model.
    """
    model = joblib.load('sentiment_model.pkl')
    return model

model = load_model()

# Create the user input interface
review_text = st.text_area('Enter a movie review to analyze:')

if st.button('Analyze'):
    if review_text:
        # Make prediction
        prediction = model.predict([review_text])
        thumbs =  '👍' if prediction[0] == 'positive' else '👎'
        st.write(f'Predicted sentiment: **{prediction[0]}**! {thumbs}')

        # Display the prediction probabilities
        prediction_proba = model.predict_proba([review_text])
        st.write('Prediction Probabilities:')
        st.write(f'Positive: {prediction_proba[0][1]:.2f}, Negative: {prediction_proba[0][0]:.2f}')
    else:
        st.error('Please enter a review to analyze.')
