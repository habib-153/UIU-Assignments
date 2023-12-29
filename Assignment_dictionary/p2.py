input_list = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

def add_values(dict_lst):
    result = {}
    for dict in dict_lst:
        item = dict['item']
        amount = dict['amount']
        if item in result:
            result[item] += amount
        else:
            result[item] = amount
    return result

output = add_values(input_list)
print(output)