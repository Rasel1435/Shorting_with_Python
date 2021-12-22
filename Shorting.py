 ##Sorting

data = [6,4,7,9,3,4,2]

def Sort(array:list):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                print(f'{array[i]} > {array[j]}')
                array[i], array[j] = array[j], array[i]
    return array

Sort(data)