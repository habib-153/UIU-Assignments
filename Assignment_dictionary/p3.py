def letter_counts(str):
    letter_count = {}
    for char in str:
        if char in letter_count:
            letter_count[char] +=1
        else:
            letter_count[char] = 1
    return letter_count

str = input()
output = letter_counts(str)
print(output)