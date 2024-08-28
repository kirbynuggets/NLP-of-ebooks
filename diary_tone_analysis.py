import glob
import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()

negativity = []
positivity = []
dates = []  # Initialize an empty list for dates

for filepath in filepaths:
    with open(filepath, "r") as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])

    # Extract the file name without the ".txt" extension
    filename = filepath.split("/")[-1].replace(".txt", "")
    dates.append(filename)

st.title("NLP of Ebooks: Tone analysis in diary")
st.subheader("Positivity")

# Corrected y parameter from string to list
pos_figure = px.line(x=dates, y=positivity, labels={"x": "ENTRIES", "y": "POSITIVITY"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")

# Corrected y parameter from string to list
neg_figure = px.line(x=dates, y=negativity, labels={"x": "ENTRIES", "y": "NEGATIVITY"})
st.plotly_chart(neg_figure)
