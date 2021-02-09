if __name__ == '__main__':
    s = input()

num= False
alpha = False
digit = False
lower = False
upper = False
for i in s:
    if i.isalnum():
        num = True
        break


for i in s:
    if i.isalpha():
        alpha = True
        break
for i in s:
    if i.isdigit():
        digit = True
        break
for i in s:
    if i.islower():
        lower= True
        break
for i in s:
    if i.isupper():
        upper= True
        break

print(num)
print(alpha)
print(digit)
print(lower)
print(upper)
