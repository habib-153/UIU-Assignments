sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
keys_to_extract = ["name", "salary"]

def extract_keys(sample_dict, keys):
    extracted_dict ={}
    for i in keys:
        if i in sample_dict:
            extracted_dict[i] = sample_dict[i]
    return extracted_dict

output = extract_keys(sample_dict,keys_to_extract)
print(output)