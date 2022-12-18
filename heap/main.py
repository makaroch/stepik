heap = []  # 1 5 7 6 5.5 3 => 1 5 3 6 5.5 7
def input_my():
    return input('задайте  операцию\n').split()

def Svap(num1, num2):
    heap[num1], heap[num2] = heap[num2], heap[num1]

def Insert(num):
    heap.append(num)
    if len(heap) == 1:
        return
    elif len(heap) == 2:
        if heap[1] < heap[0]: Svap(0, 1)
    else:
        i = len(heap) - 1
        while heap[i] < heap[ (i-1)//2 ]:
            Svap(i, ((i-1)//2))
            i = (i-1)//2
        # if heap[-1] < heap[(len(heap) - 1) // 2]:   (i-1)//2
        #     svap(heap[-1], heap[(len(heap) - 1) // 2])

def control():
    count_operations = int(input('кол-во операций\n'))

    for _ in range(count_operations):
        str_list = input_my()
        if str_list[0] == 'ExtractMax':
            print(max(heap))
        else:
            Insert(int(str_list[1]))
            print(heap)

control()
