nums = [3,4,7,8,1,2,9,5,6]
arr = sorted(nums)
print(arr)
n = len(arr)
key = int(input("Enter a number: "))
low = 0
high = n-1
found = False
while low <= high:
        mid = (low+high)//2
        if arr[mid] == key:
            print("Number found at index: ",mid)
            found = True
            break
        if arr[mid] < key:
              low = mid+1
        if arr[mid] > key:
              high = mid-1
if not found:
      print("Number not found")