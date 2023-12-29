input_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def odd_squares(lst):
    odd_square = {}
    for i in lst:
        if i%2 != 0:
            odd_square[i] = i*i
    return odd_square

output = odd_squares(input_lst)
print(output)