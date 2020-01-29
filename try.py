def mergeSort(mylist):
    if len(mylist)>1:
        mid = len(mylist)//2
        leftlist=mylist[:mid]
        rightlist=mylist[mid:]
        mergeSort(leftlist)
        mergeSort(rightlist)
        i=0
        j=0
        k=0

        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                mylist[k]=leftlist[i]
                i=i+1

            else:
                mylist[k] = rightlist[j]
                j=j+1
            k=k=1

        while i< len(leftlist):
            mylist[k] = leftlist[i]
            i=i+1
            k=k+1

        while j < len(rightlist):
            mylist[k] = rightlist[j]
            j=j+1
            k=k+1

    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)