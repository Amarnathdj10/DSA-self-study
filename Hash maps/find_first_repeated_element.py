nums = [5,1,3,4,3,5,6]

map = {}

for num in nums:
    if num not in map:
        map[num] = 1
    else:
        map[num] += 1
    if map[num] > 1:
        print(f"First repeated number is {num}")
        break
