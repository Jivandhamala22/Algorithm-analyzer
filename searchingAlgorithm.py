import time
from tkinter import messagebox

colorArray = []
global cmp
global index

try:

    def binarySearch(data, x, drawBars, timespeed, label_index, label_itemfound, label_time):
        start_time = time.time()
        #data = sorted(data)
        colorArray=['grey' for x in range(len(data))]
        #colorArray[itemIndex]='blue'

        cmp = 0
        #label_comparison.configure(text="No. of comparisons: " + str(cmp))
        index = -1
        found = False
        
        low=0
        high=len(data)-1
        global mid

        for i in range(len(data)):
            if data[i]==x:
                colorArray[i]='blue'
                break

        while not found and low <= high:

            cmp += 1
            mid = int((high + low) // 2)
            # If element is present at the middle itself
            #foundItem(mid, data) 
            colorArray[mid]='green'
            drawBars(data,colorArray)
            #label_index.configure(text= str(cmp))
            time.sleep(timespeed) 
            index = mid 
            found = True                                     
    
            # If element is smaller than mid, then it can only
            # be present in left subarray
            if data[mid] > x:
                #cmp += 1
                colorArray[mid:high+1]=['red' for x in range(high-mid+1)]
                drawBars(data,colorArray)
                #label_comparison.configure(text="No. of comparisons: " + str(cmp))
                time.sleep(timespeed)
                high = mid - 1
                found = False
    
            # Else the element can only be present in right subarray
            elif data[mid] < x:
                #cmp += 1
                colorArray[low:mid+1]=['red' for x in range(mid-low+1)]
                drawBars(data,colorArray)
                #label_comparison.configure(text="No. of comparisons: " + str(cmp))
                time.sleep(timespeed)
                low = mid + 1
                found = False

        end_time = time.time()
        
        label_index.configure(text= "No of Comparisons : " + str(cmp))

        if found:
            label_itemfound.configure(text="Element " + str(data[index]) + " found at index " + str(index))
            
        else:
            label_itemfound.configure(text="Element " + str(x) + " not found ")

        label_time.configure(text="Execution Time: " + str(round((end_time-start_time), 3))+ " sec")

        

    def linearSearch(data, x, drawBars, timespeed, label_index, label_itemfound, label_time):

        start_time = time.time()
        cmp = 0
        #label_comparison.configure(text="No. of comparisons: " + str(cmp))
        index = -1

        colorArray=['grey' for x in range(len(data))]

        for i in range(len(data)):
            if data[i]==x:
                colorArray[i]='blue'
                break

        for i in range(len(data)):
            cmp += 1
            colorArray[i]='white'
            drawBars(data,colorArray)
            time.sleep(timespeed)

            if data[i] == x:
                index = i
                colorArray[i]='green'
                #label_index.configure(text= str(cmp))
                drawBars(data,colorArray)
                time.sleep(timespeed)
                break
            else:
                colorArray[i]='red'
                label_index.configure( text=str(cmp))
                drawBars(data,colorArray)
                time.sleep(timespeed)

        end_time = time.time()
            
        label_index.configure(text= "No of Comparisons : " + str(cmp))

        if index == -1:
            label_itemfound.configure(text="Element " + str(x) + " not found ")
        else:
            label_itemfound.configure(text="Element " + str(data[index]) + " found at index " + str(index))

        label_time.configure(text="Execution Time:  " + str(round((end_time-start_time), 3))+ " sec")

except ValueError:
    messagebox.showerror("Error", 
                           "item searched cannot be found in given array")
    #itemsearchEntry.delete(0, END)

        