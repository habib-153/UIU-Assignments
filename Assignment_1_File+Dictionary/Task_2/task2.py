def getall_query(query, user_data):
    result = []
    query_parts = query.split()

    if 'link' in query_parts:
        if (query_parts[1] == 'name') and (query_parts[3]=='email'):
            column1 = 0
            column2 = 2
        elif (query_parts[1] == 'email') and (query_parts[3]=='id'):
            column1 = 2
            column2 = 1
        elif (query_parts[1] == 'name') and (query_parts[3]=='id'):
            column1 = 0
            column2 = 1

        for line in user_data:
            data = line.strip().split(', ')
            result.append({data[column1]: data[column2]})
    else: 
        if (query_parts[1] == 'name'):
            column = 0
        elif (query_parts[1] == 'email'):
            column = 2
        elif (query_parts[1] == 'id'):
            column = 1
        elif (query_parts[1] == '*'):
            column = '*'

        for line in user_data:
            data = line.strip().split(', ')
            if column == '*':
                result.append(', '.join(data))
            else:
                result.append(data[column])
    return result

f = open("c:/Python-Uni/Assignment_1_File+Dictionary/Task_2/users.txt")
user_data = f.readlines()

query = input()
output = getall_query(query, user_data)
# for i in output:
#     print(i)
w = open("c:/Python-Uni/Assignment_1_File+Dictionary/Task_2/output.txt", "w")
for i in output:
    w.write(f"{i}\n")
