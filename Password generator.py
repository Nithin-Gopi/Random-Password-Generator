#import modules
import random
import string

print('Hi, Create your new password')

length = int(input('\nEnter the length of password:'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = upper + lower + symbols + num

temp = random.sample(all,length)

password = "".join(temp)

print(password)


