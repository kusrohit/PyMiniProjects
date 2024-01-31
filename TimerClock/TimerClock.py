# Timer clock

# This is works on only command line (not graphical)

from playsound import playsound
import time

clear = "\033[2J"
clearandreturn = "\033[H"

# playsound("alarm.wav")
def alarm(seconds):
    time_elapsed = 0

    print(clear)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f'{clearandreturn}Alarm will sound in : {minutes_left:02d}:{seconds_left:02d}')

    playsound('alarm.wav')

minutes = int(input('How many minutes to wait : '))
seconds = int(input('How many seconds to wait : '))

total_seconds = minutes * 60 + seconds
alarm(total_seconds)



# Credit : Tech with Tim (On Youtube)