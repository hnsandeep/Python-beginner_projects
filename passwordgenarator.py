import random
import string
total =  string.ascii_letters + string.digits + string.punctuation
# `length = 16` is setting the length of the password to be generated to 16 characters.
length = 16
password = "".join(random.sample(total, length))
print(password)
