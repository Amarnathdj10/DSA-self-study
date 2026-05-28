nums = [3,4,7,8,1,2,9,5,6]
key = int(input("Enter number to search: "))
keyfound = 0
for i in range(len(nums)):
    if nums[i] == key:
        print(f"Number found at index {i}")
        keyfound = 1
        break
if keyfound == 0:
    print('Number not found')