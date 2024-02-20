import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ketutu dha iruken...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        print("Iru ya badhil solren...")
        query = recognizer.recognize_google(audio)
        print(f"You: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't request results. Check your internet connection.")
        return ""

def speak(response):
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

def assistant_response(user_input):
    responses = {
        "hi": "Hello! How can I assist you?",
        "saptingala": "saaptaen saaptaen. neenga saaptingala?",
        "what's the time": "It's time to answer your queries!",
        "Nee yaaru": "Naa Suhail oda assistant"
        }

    if user_input in responses:
        return responses[user_input]
    else:
        return "Sorry daa! Nee enna solrey enaku edhuvum puriyalai."

def main():
    print("Welcome to your Google Assistant-like application!")
    print("You can start speaking. Say 'exit' to end the conversation.")

    while True:
        user_input = listen()
        if user_input == 'ponga bro':
            speak("Byeee mamae, durrrrr")
            break

        response = assistant_response(user_input)
        print("Assistant:", response)
        speak(response)

if __name__ == "__main__":
    main()

