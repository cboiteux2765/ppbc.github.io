import datetime

f = open('task.txt', 'a')

f.write(f'{datetime.datetime.now()} - Script ran')