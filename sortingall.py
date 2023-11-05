arr=[12,34,54,2,3]
def bubble():
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)
def selection():
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min]):
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    print(arr)
def insertion():
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while(j>=0 and temp<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    print(arr)
def quick(arr,left,right):
    pos_partision=partision(arr,left,right)
    quick(arr,left,pos_partision-1)
    quick(arr,pos_partision+1,right)
def partision(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]
    while i<j:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i
arr=[22,11,88,66,55,77,33,44]
# l=length(arr)
bubble()
selection()
insertion()
quick(arr,0,len(arr)-1)
print(arr)