import time #to freeze our program

user = input('Enter your name: ') 
print(f'Hello {user}!') # making it a little friendly!

time.sleep(2) # making it natural

my_time = int(input('Enter how many seconds you want :) : '))

for x in range(my_time,0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int( x / 3600 )
    print(f'{hours:02}:{minutes:02}:{seconds:02}') # 02 because we want a 0 before our number
    time.sleep(1) # each second print a number pls :)

print ('Times Up!')
time.sleep(1)
print(f'Bye for now {user}') # being friendly is important !

