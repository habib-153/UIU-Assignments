str = input()

def word_count(str):
    str_lst = list(str.split())
    frequencies = {}
    for i in str_lst:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    return frequencies

output = (word_count(str))
print(output)