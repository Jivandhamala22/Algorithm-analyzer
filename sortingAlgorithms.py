import time

def BubbleSort(data, drawBars, timespeed, label_comparison, label_index):
    start= time.time()
    cmp = 0
    swp = 0
    #label_index.configure(text=  str(cmp))

    for i in range (len(data) - 1):
        flag = False
        for j in range (0, len(data) - i - 1):
            #cmp+=1
            #label_index.configure(text= str(cmp))
            if (data[j] > data[j+1]):
                swp += 1
                data[j] , data[j+1] = data[j+1] , data[j]
                flag = True

                drawBars(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(timespeed)

        if(flag!=True):
            break

    end = time.time()
    label_comparison.configure(text= "No of times elements swapped:  " +  str(swp))
    label_index.configure(text="Execution Time: " + str(round((end-start), 2)) + " sec")



def merge_sort(data, drawBars, timespeed,label_comparison, label_index):
    merge_sort_alg(data, 0 , len(data)- 1, drawBars, timespeed, label_comparison, label_index)

def merge_sort_alg(data, left, right, drawBars, timespeed, label_comparison,  label_index):
    start = time.time()
    if left < right:
        middle = (left + right) // 2

        merge_sort_alg(data, left, middle, drawBars, timespeed, label_comparison, label_index)

        merge_sort_alg(data, middle + 1, right, drawBars, timespeed,label_comparison, label_index)

        merge(data, left, middle, right, drawBars, timespeed, label_index)

    end = time.time()
    #.configure(text= "No of times elements swapped:  " +  str(swp))
    label_index.configure(text= "Execution Time: " + str(round((end-start), 2)) + " sec")


def merge(data, left, middle, right, drawBars, timespeed, label_index):
    cmp = 0
    drawBars(data, getColorArray(len(data), left, middle, right))
    time.sleep(timespeed)

    leftPart = data[left: middle+1]
    rightPart = data[middle+1: right+1]
    leftIndex = rightIndex = 0

    for dataIndex in range(left, right+1):
        if leftIndex < len(leftPart) and rightIndex < len(rightPart):
            if leftPart[leftIndex] <= rightPart[rightIndex]:
                data[dataIndex] = leftPart[leftIndex]
                leftIndex += 1
                cmp += 1
                #label_index.configure(text= str(cmp))
            else:
                data[dataIndex] = rightPart[rightIndex]
                rightIndex += 1

        elif leftIndex < len(leftPart):
            data[dataIndex] = leftPart[leftIndex]
            leftIndex += 1

        else:
          data[dataIndex] = rightPart[rightIndex]
          rightIndex += 1

        #label_index.configure(text= str(cmp))
          
    drawBars(data, ['green' if x >= left and x<= right else 'white' for x in range(len(data))])
    time.sleep(timespeed)

def getColorArray(length, left, middle, right):
    colorArray = []
    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append('yellow')
            else:
                colorArray.append('pink')

        else:
            colorArray.append('white')

    return colorArray

def QuickSort(data, head, tail, drawBars, timespeed,label_comparison, label_index):
    start = time.time()
    if head < tail:
        partitionIdx = Partition(data, head, tail, drawBars, timespeed)

        #left partition
        QuickSort(data, head, partitionIdx-1, drawBars, timespeed,label_comparison, label_index)

        #right partition
        QuickSort(data, partitionIdx+1, tail, drawBars, timespeed,label_comparison, label_index)
    end = time.time()
    #label_comparison.configure(text= "No of times elements swapped:  " +  str(cmp))
    label_index.configure(text="Execution Time: " +  str(round((end-start), 2)) + " sec")

def Partition(data, head, tail, drawBars, timespeed):
    cmp = 0
    border = head
    pivot = data[tail]

    drawBars(data, getColorArrayQuick(len(data), head, tail, border, border))
    time.sleep(timespeed)
    #label_index.configure(text= str(cmp))
    for j in range(head,tail):
        if data[j] <= pivot:
            drawBars(data, getColorArrayQuick( len(data), head, tail, border,j, True))
            time.sleep(timespeed)

            data[border] ,data[j] = data[j] , data[border]
            border += 1
        cmp += 1
        drawBars(data, getColorArrayQuick( len(data), head, tail, border,j))
        time.sleep(timespeed)

    #swap pivot with border value
    drawBars(data, getColorArrayQuick( len(data), head, tail, border,tail, True))
    time.sleep(timespeed)
    data[border], data[tail] = data[tail], data[border]

    return border

def getColorArrayQuick(dataLen, head, tail, border, currentIdx, isSwapping = False):
    colorArray = []
    for i in range(dataLen):

        #base color
        if i>=head and i<=tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'

        elif i == border:
            colorArray[i] = 'red'

        elif i == currentIdx:
            colorArray[i] = 'yellow'

        if isSwapping:
            if i == border or i == currentIdx:
                colorArray[i] = 'green'
    return colorArray


    