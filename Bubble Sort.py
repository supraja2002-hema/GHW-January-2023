def bubbleSort(lst):
    n=len(lst)
    swapped=False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                swapped=True
        if not swapped:
            return

lst=[55,31,48,2,43,21]
bubbleSort(lst)
print(lst)