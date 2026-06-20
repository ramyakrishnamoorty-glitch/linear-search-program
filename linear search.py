def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        return -1
number =[1,2,3,4,5]
target = 8
result = linear_search(number,target)
if result != -1:
    print("Element found at index:{result}")
else:
    print("element is not found in the array")

     