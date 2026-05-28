nums = [1,2,3,4,1]
map = {}

for num in nums:
    if num not in map:
        map[num] = 1
    else:
        map[num] += 1

for i in nums:
    if map[i] > 1:
        print(f"Duplicate of {i} found")
    else:
        print(f"No duplicates for {i}")