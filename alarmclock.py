import time
import pygame
import datetime

def set_alarm(alarm_time, sound_file):
    """Set the alarm for the specified time."""
    print(f"Alarm set for {alarm_time}.")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Alarm ringing!")
            pygame.mixer.music.load(sound_file)  # Load your alarm sound file
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break
        time.sleep(1)

#set the alarm time and sound file
alarm_time = input("Enter the alarm time (HH:MM:SS): ")
sound_file = 
set_alarm(alarm_time, sound_file)
pygame.quit()