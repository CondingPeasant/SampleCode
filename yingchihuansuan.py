import math
cm = input()
cm = float(cm)/100
foot = cm*144/145/0.3048
foot_seg,foot = math.modf(foot)
inch = foot_seg * 12
inch = int(inch)
foot = int(foot)
print(foot,inch)


# cm=input()
# cm=float(cm)/100
# f=cm*144/0.3048/145
# inch=(f-int(f))*12
# inch=int(inch)
# f=int(f)
# print(f,inch)