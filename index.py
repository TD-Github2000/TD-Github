import pyttsx3

def text_to_speech(text, rate=150):
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)  # ความเร็วการพูด (default=200)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    input_text = input("Enter text to convert to speech: ")
    text_to_speech(input_text)
