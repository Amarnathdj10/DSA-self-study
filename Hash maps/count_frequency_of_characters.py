word = "banana"
map = {}

for letter in word:
    if letter not in map:
        map[letter] = 1
    else:
        map[letter] += 1

for i in map:
    print(f"Frequency of {i}: ",map[i])