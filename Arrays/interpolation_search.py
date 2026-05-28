nums = [3,4,7,8,1,2,9,5,6]
arr = sorted(nums)
print(arr)
n = len(arr)
key = int(input("Enter a number: "))
low = 0
high = n-1
found = False
while low <= high and key >= arr[low] and key <= arr[high]:
        pos = low + ((key-arr[low])*(high-low))//(arr[high]-arr[low])
        if arr[pos] == key:
            print("Key found at index: ",pos)
            found = True
            break
        if arr[pos] < key:
              low = pos+1
        if arr[pos] > key:
              high = pos-1
if not found:
      print('Number not found')