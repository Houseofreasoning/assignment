import datetime
import random
#get current time
current_time = datetime.datetime.now()
#get hour
hour = current_time.hour
#greet
if hour>=0 and hour <12:
    greet="Good morning!"
    print(greet)
elif hour>=12 and hour <18:
    greet="Good afternnon!"
    print(greet)
else:
    greet="Good evening!"
    print(greet)
print()

def weekday():
    day_names=['Monday','Tuesday','Wednesday','Thurday','Friday','Saturday','Sunday']
    today=datetime.datetime.now().weekday()
    return day_names[today]
def messageoftheday():
    day = weekday()
    if day in ['Monday','Tuesday','Wednesday','Thurday','Friday']:
        print(f'Today is {day} let go to work')
    elif day == 'Satueday':
        print(f'Today is {day} let go to work')
    else:
        print(f'Happy {day} let go to church')
messageoftheday()