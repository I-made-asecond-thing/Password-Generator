import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "%#(){}[]"
numbers = "0123456789"

all = lower + upper + symbols + numbers

length = 12
password = "".join(random.sample(all,length))
print(password)
