from datetime import datetime

# 1. Gör ett program som skriver ut dagens datum och tid


# now = datetime.now()

# now = now.strftime("%Y-%m-%d %H:%M")

# print(f"The current date and time is {now}")


# 2. Prova olika sätt att skriva ut tid/datum


# now = datetime.now()

# date = now.date()
# time = now.time()

# now = now.strftime("%Y-%m-%d %H:%M")

# print(f"The current date and time is {now}")
# print(f"The current date is {date}")
# print(f"The current time is {time}")


# 3. Gör så klockan uppdateras automatiskt
import msvcrt
import os
import time

# while not msvcrt.kbhit():
#     os.system("cls")
#     now = datetime.now()
#     actuall_time = now.time().strftime("%H:%M:%S")
#     print(actuall_time)
#     time.sleep(1)
# msvcrt.getch()

# 4. Gör en modul som ändrar färg (kolla projekt här på CR)

from Colors import Colors

# 5. Skapa ett färgstarkt program som använder färg samt något mer du lärt dig (se colors.txt nedan)

# now = datetime.now()

# rainbow = [
#     Colors.RED,
#     Colors.YELLOW,
#     Colors.GREEN,
#     Colors.CYAN,
#     Colors.BLUE,
#     Colors.MAGENTA
# ]

# color_index = 0


# def clock_time(current_time, color):
#     os.system("cls")
#     print(color+ f"{current_time}")
#     return

# while not msvcrt.kbhit():
#     current_time = now.time()
#     color = rainbow[color_index]
#     color_index = (color_index + 1) % len(rainbow)

#     clock_time(current_time, color)

#     time.sleep(1)
# msvcrt.getch()

# 6. Uppdatera gärna något annat gammalt program med getwch() och färger!

# weight = float(input("Skriv din vikt i kg: "))
# height = float(input("Skriv din längd i m: ")) 

# bmi = weight/(height**2)

# print(Colors.RÖD + f"Din BMI är {bmi}")


# 7. ÖVERKURS: Skapa en egen modul och importera till ett program

from Colors import Colors



