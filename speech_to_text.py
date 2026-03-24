import os
import sys

import speech_recognition as sr


def transcribe_audio(file_path: str) -> str:
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File not found.")

    if not file_path.lower().endswith(".wav"):
        raise ValueError("Please provide a .wav audio file.")

    recognizer = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)

    return recognizer.recognize_google(audio_data)


def transcribe_microphone() -> str:
    import time

    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1
    transcriptions = []

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("🎤 Listening...")

            while True:
                try:
                    audio = recognizer.listen(source, timeout=5)
                    text = recognizer.recognize_google(audio)
                    print(f"You said: {text}")

                    if "stop" in text.lower():
                        break

                    transcriptions.append(text)
                    time.sleep(0.3)
                except sr.UnknownValueError:
                    time.sleep(0.3)
                    continue
                except sr.WaitTimeoutError:
                    time.sleep(0.3)
                    continue
                except KeyboardInterrupt:
                    print("\nStopping microphone transcription.")
                    break
    except OSError:
        raise OSError("Microphone not found or unavailable.")

    print("Final transcription ready")
    return " ".join(transcriptions)


def save_transcription(text: str, output_file: str = "output.txt") -> None:
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)


def main() -> None:
    print("Choose input method:")
    print("1. Audio file")
    print("2. Microphone")
    choice = input("Enter your choice (1 or 2): ").strip()

    try:
        if choice == "1":
            if len(sys.argv) > 1:
                audio_file = sys.argv[1]
            else:
                audio_file = input("Enter path to .wav audio file: ").strip()

            text = transcribe_audio(audio_file)
        elif choice == "2":
            text = transcribe_microphone()
        else:
            print("Error: Invalid choice.")
            return

        print(f"📝 Transcribed Text: {text}")

        save_choice = input("Save transcription to output.txt? (y/n): ").strip().lower()
        if save_choice == "y":
            save_transcription(text)
            print("Transcription saved to output.txt")
    except FileNotFoundError as error:
        print(f"Error: {error}")
    except ValueError as error:
        print(f"Error: {error}")
    except sr.WaitTimeoutError:
        print("Error: No speech detected within the timeout period.")
    except sr.UnknownValueError:
        print("Error: No speech detected or could not understand the audio.")
    except sr.RequestError as error:
        print(f"Error: Google Speech API request failed: {error}")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
