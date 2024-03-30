import random
lower="qwertyuiopasdfghjklzxcvbnm"
upper="QWERTYUIOPASDFGHJKLZXCVBNM"
number="1234567890"
symboles="!@#$%^&*()]}[{?/>.<,+=_-`~"
length=int(input("enter the length of the password:"))
all=lower+upper+number+symboles
password="".join(random.sample(all,length))
print("The password:",password)



































































