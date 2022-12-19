heap = []  # 1 5 7 6 5.5 3 => 1 5 3 6 5.5 7
def input_my():
    return input('задайте  операцию\n').split()

def Svap(num1, num2):
    if num1 == -1 or num2 == -1: # из за касяка с индексом может приодить -1 из-за этого меняем местами не те элементы
        return                   # соот ветственно если пришла -1 ничего не нужно менять местами
    heap[num1], heap[num2] = heap[num2], heap[num1]

def Insert(num):
    heap.append(num)
    if len(heap) == 1:
        return
    elif len(heap) == 2:
        if heap[1] < heap[0]: Svap(0, 1)
    else:
        i = len(heap) - 1
        while heap[i] < heap[((i-1)//2)]:
            Svap(i, ((i-1)//2) )
            i = (i-1)//2
def heap_max_index(heap_list: list):
    i = len(heap_list) - 1
    max_index = i
    count_operant = 0
    while (2*i + 1) > (len(heap_list) - 1):
        if heap_list[max_index] < heap_list[i]: max_index = i
        i -= 1
        count_operant +=1
    print(count_operant)
    return max_index


def control():
    count_operations = int(input('кол-во операций\n'))

    for _ in range(count_operations):
        str_list = input_my()
        if str_list[0] == 'ExtractMax':
            print(heap[heap_max_index(heap)])
        else:
            Insert(int(str_list[1]))
            print(heap)

control()


