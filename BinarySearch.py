def BubbleSort(arr,n):
    for i in range(n):
        for f in range(n-i-1):
            if(arr[f]>arr[f+1]):
                (arr[f],arr[f+1])=(arr[f+1],arr[f])
    return arr

def BinarySearch(arr,size,element):

    start=0
    end=size-1
    while(start<=end):

        mid=int((start+end)/2)

        if(arr[mid]==element):

            return mid
        if(arr[mid]<element):

            start=mid+1
        
        else:
            end=mid-1


arr=[2,3231,1231,21,231,2,131,312,0,231,23]
arr=BubbleSort(arr,len(arr))
print(arr)
f=BinarySearch(arr,len(arr),1231)
print(f)

