import openai
from gtts import gTTS
import os
import speech_recognition as sr
import threading
from playsound import playsound

# Set your OpenAI API key here
openai.api_key = "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"

def generate_response(query):
    # Use your GBT-4 model to generate a response based on the input query
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Specify your engine
        prompt=query,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def text_to_speech(text, filename="output.mp3"):
    # Convert text to speech using gTTS
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    return filename

def play_audio(filename):
    # Play the generated audio file using playsound
    playsound(filename)

def speech_to_text():
    # Use SpeechRecognition library to recognize speech input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        try:
            audio = r.listen(source, timeout=None)
            print("Recognition started")
            query = r.recognize_google(audio)
            print("You said:", query)
            return query
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

def input_thread():
    # This thread listens for keyboard input to finalize speech input
    input("Press Enter to finalize speech input\n")

# Example usage
while True:
    # Start the speech recognition process in a separate thread
    speech_thread = threading.Thread(target=speech_to_text)
    speech_thread.start()

    # Wait for keyboard input to finalize speech input
    input_thread()

    # Stop listening for speech input after Enter is pressed
    speech_thread.join()

    # Process user input
    user_input = speech_to_text()

    # Generate response
    response = generate_response(user_input)

    # Text to speech
    audio_file = text_to_speech(response)

    # Play audio
    play_audio(audio_file)
