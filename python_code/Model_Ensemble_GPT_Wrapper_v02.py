pip install sounddevice SpeechRecognition gtts requests

import sounddevice as sd
import speech_recognition as sr
import requests
from gtts import gTTS
import os
from scipy.io.wavfile import write
import numpy as np

# Record voice
def record_voice(duration=5, fs=44100):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    write('output.wav', fs, recording)  # Save as WAV file

# Convert speech to text
def speech_to_text(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Error; {e}"

# Send text to custom GPT model and get response
def get_gpt_response(text):
    # Replace with your actual endpoint and API key
    endpoint = "YOUR_CUSTOM_GPT_ENDPOINT"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    data = {"prompt": text, "max_tokens": 50}  # Adjust parameters as needed

    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['text'].strip()
    else:
        return "Error in GPT response"

# Convert text to speech
def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("response.mp3")
    os.system("start response.mp3")

# Main function
def main():
    record_voice()
    text = speech_to_text("output.wav")
    print("You said:", text)

    gpt_response = get_gpt_response(text)
    print("GPT Response:", gpt_response)

    text_to_speech(gpt_response)

if __name__ == "__main__":
    main()
