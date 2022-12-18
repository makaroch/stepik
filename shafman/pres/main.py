string = input()

dikt = {}
for item in string:
    if item in dikt:
        dikt[item] += 1
    else:
        dikt[item] = 1
list_1 = []
for k,v in dikt.items():
    list_1.append((k, v))

def my_sort(s_list):
    s_list.sort(key=lambda x: (x[1], x[0]))

my_sort(list_1)
# print(list_1)

bin_list = []

while len(list_1) > 1:
    x = list_1[0][0] # буква
    y = list_1[1][0] # буква
    if list_1[0][1] >= list_1[1][1]:
        bin_list.append((x, 0))
        bin_list.append((y, 1))
    else:
        bin_list.append((x, 1))
        bin_list.append((y, 0))
    (symbol, vel) = (x + y, list_1[0][1] + list_1[1][1])
    list_1.append((symbol, vel))
    list_1.pop(0)
    list_1.pop(0)
    my_sort(list_1)
# print(bin_list)
bin_dict = {}
for item in bin_list:
    for char in item[0]:
        if char in bin_dict:
            bin_dict[char] += str(item[1])
        else:
            bin_dict[char] = str(item[1])
# print(bin_dict)
res_str = ''
for char in string:
    res_str += bin_dict[char]
print(f"{len(dikt)} {len(res_str)}")
for k, v in bin_dict.items():
    print(f"{k}: {v}")
print(res_str)