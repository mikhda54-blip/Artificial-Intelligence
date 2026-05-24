from tkinter import *
from deep_translator import GoogleTranslator

# Translation function
def translate_text():

    text = input_box.get("1.0", END)

    translated = GoogleTranslator(
        source='english',
        target='hindi'
    ).translate(text)

    output_box.delete("1.0", END)

    output_box.insert(END, translated)

# Create window
root = Tk()

root.title("AI Language Translator")

root.geometry("500x400")

# Input label
Label(root, text="Enter English Text").pack(pady=5)

# Input box
input_box = Text(root, height=5, width=40)
input_box.pack()

# Translate button
Button(
    root,
    text="Translate",
    command=translate_text
).pack(pady=10)

# Output label
Label(root, text="Hindi Translation").pack(pady=5)

# Output box
output_box = Text(root, height=5, width=40)
output_box.pack()

# Run app
root.mainloop()