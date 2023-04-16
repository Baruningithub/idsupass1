import string
import random
def genpswd(length,n):
    for i in range(n):
        ch=string.ascii_letters+string.digits
        print(''.join(random.choices(ch,k=length)))

genpswd(8,18)
