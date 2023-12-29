original_student_data = {
    'Emma': {'name': 'Emma', 'major': 'Computer Science', 'cgpa': 3.8, 'completed_credits': 90},
    'Daniel': {'name': 'Daniel', 'major': 'Electrical Engineering', 'cgpa': 3.5, 'completed_credits': 75},
    'Sophia': {'name': 'Sophia', 'major': 'Mechanical Engineering', 'cgpa': 3.2, 'completed_credits': 60}
}

def transform_student_data(student_data):
    transformed_data ={}
    cgpa = [info['cgpa'] for info in student_data.values()]
    sorted_cgpa = sorted(cgpa, reverse=True)
    
    for i in sorted_cgpa:
        for key, value in student_data.items():
            if value['cgpa'] == i:
                transformed_data[key] = {'cgpa': value['cgpa'], 'completed_credits': value['completed_credits']}

    return transformed_data

output = transform_student_data(original_student_data)
print(f"Transformed student data: \n{output}")