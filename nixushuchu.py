num=int(input())
one = num%10
hundred = num//100
ten = num//10%10
number = one*100+ten*10+hundred
print(number)
