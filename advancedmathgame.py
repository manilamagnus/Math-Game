#advanced math game
import random

def exmp1 (pizza, sausage):
    return pizza + sausage
def sub (pizza, sausage):
    return pizza - sausage
def mul (pizza, sausage):
    return pizza * sausage
def div (pizza, sausage):
    return pizza / sausage

dic = {}
dic["+"] = exmp1
dic["-"] = sub
dic["*"] = mul
dic["/"] = div

pizza = random.randint(1, 10)
sausage = random.randint(1, 10)
sign = random.choice(list(dic.keys()))

ans = dic[sign](pizza, sausage)

if sign == "/":
    ans = pizza
    pizza = pizza * sausage

    
print("answer the following")
input = input(str(pizza) + sign + str(sausage) + " = ")
    
if int(input) == ans:
    print("correct")
else:
    print("dumbfuck")    

