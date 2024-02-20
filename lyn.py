import os

def recognize_speech():
    os.system("cls" if os.name == "nt" else "clear")  # Clear the screen
    print("Listening... (Press Enter when done)")
    input()  # Wait for user to press Enter
    print("Recognizing...")

    # Simulate voice recognition by reading input from user
    command = input("You said: ").lower()
    return command

def speak(text):
    print("Siri:", text)

def open_email():
    speak("Opening email...")
    # Your code to open the email application goes here
    print("Email opened.")

def create_file():
    speak("Creating a file...")
    file_name = input("Enter file name: ")
    with open(file_name, 'w') as file:
        file.write("This is a new file created by the virtual assistant.")
    print(f"File '{file_name}' created.")

def siri():
    speak("Hi, I'm Siri. How can I help you today?")
    while True:
        command = recognize_speech()

        if "open email" in command:
            open_email()
        elif "create file" in command:
            create_file()
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    siri()
