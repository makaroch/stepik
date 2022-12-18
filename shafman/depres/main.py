caunt_char, cod = input("dddd").split()
dikt_char = {}
for _ in range(int(caunt_char)):
    v, k = input('символ код').split(': ')
    dikt_char[k] = v
print(dikt_char)
str_encoded = input()
left_border = 0
res = ''
right_border = 1
while right_border < len(str_encoded) + 1:
    if str_encoded[left_border:right_border] in dikt_char:
       res += dikt_char[str_encoded[left_border:right_border]]
       left_border = right_border
       right_border += 1
    else:
        right_border += 1
print(res)
