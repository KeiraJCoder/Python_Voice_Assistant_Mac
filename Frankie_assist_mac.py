import openai
import speech_recognition as sr
import subprocess
import os

# Load your OpenAI API Key from environment variable for better security
openai.api_key = os.getenv("OPENAI_API_KEY")

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except Exception as e:
        print(f'Skipping, encountered error during transcription: {e}')

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Consider checking for a newer engine version
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text

def speak_text(text):
    subprocess.run(['say', text])

def main():
    print("Ensure your OPENAI_API_KEY environment variable is set.")
    while True:
        print("Say 'Hey Frankie' to start recording your question....")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "hey frankie":
                    filename = 'input.wav'
                    print("Say your question....")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())
                            
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print(f"You said: {text}")
                        
                        response = generate_response(text)
                        print(f"Frankie says: {response}")
                        
                        speak_text(response)
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("OPENAI_API_KEY environment variable not set. Exiting.")
    else:
        main()


