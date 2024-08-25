from gtts import gTTS
import os

def text_to_audio(text, filename='output.mp3'):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print(f'Audio saved as {filename}')

# Example usage
text_to_audio('Hello, this is a test audio.')
