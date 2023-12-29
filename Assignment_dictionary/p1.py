sample = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
sorted_v = sorted(list(sample.values()))
sorted_dict ={}

for i in sorted_v:
    for key,value in sample.items():
        if i == value:
            sorted_dict[key] = i

output = list(sorted_dict.items())
print(output)