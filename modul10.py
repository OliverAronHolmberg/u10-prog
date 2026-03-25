from datetime import datetime
import msvcrt
import msvcrt
import os
import time

# 1. Gör ett program som skriver ut dagens datum och tid


now = datetime.now()

now = now.strftime("%Y-%m-%d %H:%M")

print(f"The current date and time is {now}")


# 2. Prova olika sätt att skriva ut tid/datum


now = datetime.now()

date = now.date()
current_time = now.time()

now = now.strftime("%Y-%m-%d %H:%M")

print(f"The current date and time is {now}")
print(f"The current date is {date}")
print(f"The current time is {current_time}")


# 3. Gör så klockan uppdateras automatiskt


while not msvcrt.kbhit():
    os.system("cls")
    now = datetime.now()
    actuall_time = now.time().strftime("%H:%M:%S")
    print(actuall_time)
    time.sleep(1)
msvcrt.getch()


# 4. Gör ett tidtagarur



running = False
start_time = None
total_passed_time = 0 


while True:
    key = msvcrt.getwch()
    
    if key == '\r': 
        if running:
            diff = datetime.now() - start_time
            total_passed_time += diff.total_seconds()
        break
    
    else:
        if not running:
            start_time = datetime.now()
            running = True
            print(">> Startat")
        else:
            stop_time = datetime.now()
            diff = stop_time - start_time
            total_passed_time += diff.total_seconds()
            running = False
            print(f"Pausat vid: {total_passed_time:.2f}s")


# 5. Lägg till klockan i ett annat program/spel du har skapat

class Color:
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

list = ["item1", "item2", "item3"]

def write_list():
    os.system("cls")
    for i, name in enumerate(list, 1):
        print(Color.RED +f"{i}. {name}")
    time.sleep(1)

def show_clock():
    
    while not msvcrt.kbhit():
        os.system("cls")
        current_time = datetime.now().strftime("%H:%M:%S")
        
        print(Color.GREEN + "Klockan")
        print(f"{current_time}")
        print("Tryck på valfri tangent för att gå tillbaka till menyn" + Color.RESET)
        
        time.sleep(0.5)
    msvcrt.getwch()

while True:
    os.system("cls")
    print(Color.BLUE + "Choose an alternative, 1 -Write list or 2- Show Clock or 3 - Exit", end="")
    keys = msvcrt.getwch()
    if keys == "1":
        write_list()
    elif keys == "2":
        show_clock()
    elif keys == "3":
        break
    else:
        continue

# 6. ÖVERKURS: Skriv ett program som frågar användaren efter ett specifikt datum (månad, dag och år) och sedan beräknar antalet dagar mellan det datumet och dagens datum.

while True:
    try:
        day = int(input("Write the number of a day, (ex. 05, return to quit): "))
        month = int(input("Write a number of a month (ex. 04, return to quit): "))
        year = int(input("Write a year, (ex. 1939, return to quit): "))
    except:
        break
    target_date = datetime(year, month, day).date()

    todays_date = datetime.now().date()

    diff = abs(todays_date-target_date)
    days_diff = diff.days

    print(f"Det är {days_diff} dagar mellan {target_date} och {todays_date}")

# 7. ÖVERKURS: Gör en larmklocka eller timer där man kan ställa in tid för nedräkning. Något ska hända när tiden är ute
while True:
    try:
        seconds_input = int(input("Hur många sekunder ska timern vara? (t.ex. 13, return to quit): "))
    except:
        break

    end_time = datetime.now().timestamp() + seconds_input

    while datetime.now().timestamp() <end_time:
        os.system("cls")

        time_left = int(end_time - datetime.now().timestamp())
        print(f"{time_left} seconds left")

        time.sleep(1)
    print("Timer has ended")

