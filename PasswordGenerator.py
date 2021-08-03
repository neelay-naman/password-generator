import random

uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowercase = uppercase.lower()
numericals = "1234567890"
symbols = "!@#$%^&*_+-=\\|/.,<>~`"

u, l , num , sym = False,False,False,False

print('Do you want a complex password (y/n)')
answer = input().split()
answer = answer[0].lower()
if answer == 'y':
    u, l, num, sym = True,True,True,True
elif answer == 'n':
    u, l = True, True
else:
    print('Wrong Input, write "y" for yes and "n" for no')
    u, l = True,True

all = ""

if u:
    all += uppercase
if l:
    all += lowercase
if num:
    all += numericals
if sym:
    all += symbols

length_of_password = 20
amount_of_password = 10

for x in range(amount_of_password):
    password = "".join(random.sample(all, length_of_password))
    print(password)
