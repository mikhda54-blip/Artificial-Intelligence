from tkinter import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Questions
questions = [
    "What is AI?",
    "What is Python?",
    "What is machine learning?",
    "Who developed Python?",
    "What is chatbot?"
]

# Answers
answers = [
    "AI means Artificial Intelligence.",
    "Python is a programming language.",
    "Machine learning allows computers to learn from data.",
    "Python was developed by Guido van Rossum.",
    "A chatbot is a computer program that talks with users."
]

# Chatbot function
def chatbot():

    user_question = entry.get()

    all_questions = questions + [user_question]

    vectorizer = CountVectorizer()

    vectors = vectorizer.fit_transform(all_questions)

    similarity = cosine_similarity(vectors[-1], vectors[:-1])

    index = np.argmax(similarity)

    response = answers[index]

    output.config(text=response)

# Create window
root = Tk()

root.title("FAQ Chatbot")

root.geometry("500x300")

# Heading
Label(
    root,
    text="FAQ Chatbot",
    font=("Arial", 16)
).pack(pady=10)

# Input box
entry = Entry(root, width=50)
entry.pack(pady=10)

# Ask button
Button(
    root,
    text="Ask",
    command=chatbot
).pack()

# Output label
output = Label(
    root,
    text="",
    wraplength=400,
    font=("Arial", 12)
)

output.pack(pady=20)

# Run app
root.mainloop()