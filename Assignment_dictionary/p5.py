lst1 = ["Black", "Red", "Maroon", "Yellow"]
lst2 = ["#000000", "#FF0000", "#800000","#FFFF00"]

def lst_dict(lst1, lst2):
    lst = []
    for i in range(len(lst1)):
        color_dict = {'color_name': lst1[i], 'color_code': lst2[i]}
        lst.append(color_dict)
    return lst

output = lst_dict(lst1, lst2)
print(output)

