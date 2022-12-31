import random 

luckynumber = random.randint(1,100)

fortunenumber=random.randint(1,3)
fortunetext=''

if fortunenumber==1:
    fortunetext='You will have a great day!'

if fortunenumber==2:
    fortunetext='You will get married this year !'
if fortunenumber==3:
    fortunetext='Today will be a tough day!'


print(f'{fortunetext} Your Lucky no. is {luckynumber}')