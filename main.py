with open("case.txt","r") as f:
    #read first line
    data = [int(value) for value in next(f).split()]
    #case > 1 line
    # array = [[int(value) for value in line.split()] for line in f]
    print (data)

def partition(data,low,high):
    i = (low - 1)   #index
    pivot = data[high]

    for j in range(low,high):
        #jika nilai sekarang > dari tumpuan
        if data[j] > pivot:
            i = i + 1
            data[i],data[j] = data[j],data[i]

    data[i+1],data[high] = data[high],data[i+1]
    return (i + 1)

def quickSort (data,low,high):
    if low < high:
        pi = partition(data,low,high)

        quickSort(data,low, pi-1)
        quickSort(data,pi+1, high)

#driver
n = len(data)
quickSort(data,0,n-1)
print (data)