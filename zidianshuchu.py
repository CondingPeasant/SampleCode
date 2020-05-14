num0 = input()
count = 0
for i in num0:
    count += int(i)
# print(count)
dict0 = {'1':'yi', '2':'er', '3':'san','4':'si','5':'wu','6':'liu','7':'qi','8':'ba','9':'jiu','0':'ling'}
name = ''
for i in str(count):
    name += str(dict0[i])
    name += ' '

print(name.rstrip())


