import time
import pygame
import datetime

def set_alarm(alarm_time, sound_file):
    """Set the alarm for the specified time."""
    print(f"Alarm set for {alarm_time}.")
    pygame.mixer.init()  # Initialize the mixer
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Alarm ringing!")
            try:
                pygame.mixer.music.load(sound_file)  # Load your alarm sound file
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            except pygame.error as e:
                print(f"Error playing sound: {e}")
            break
        time.sleep(1)

if __name__ == "__main__":
    # Input alarm time in 24-hour format
    alarm_time = input("Enter the alarm time in 24-hour format (HH:MM:SS): ")
    sound_file = "gorila-315977.mp3"  # Replace with your sound file path

    try:
        # Validate the time format
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
        set_alarm(alarm_time, sound_file)
    except ValueError:
        print("Invalid time format. Please enter the time in HH:MM:SS 24-hour format.")
    finally:
        pygame.quit()