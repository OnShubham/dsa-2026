def bubble_sort(arr):
    lenght = len(arr)
    
    for i in range(lenght - 1, -1 , -1 ):
        did_swap = False
        
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] =arr[j + 1], arr[j]
                did_swap = True
        
        if not did_swap:
            break
    print(arr)
        

arr = [12,2,1,44,3,2,4,55,22,5]
bubble_sort(arr)