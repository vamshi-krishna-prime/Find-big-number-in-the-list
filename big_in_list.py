
list = [["a", 9], ["b", 6], ["c", 4] , ["d", 3]]
big = 0
letter = " "
for num in list[:1]:
    big = num[1]
    letter = num[0]
    for numb in list[1:]:
        if numb[1] > big:
            big = numb[1]
            letter = numb[0]
print(big)
print(letter)
