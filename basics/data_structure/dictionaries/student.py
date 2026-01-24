student_info = {
    'name': 'John Doe',
    'age': 20,
    'major': 'Computer Science',
    'gpa': 3.8,
    'is_on': True
}

# accessing the dictionary
print(student_info)
print(student_info['name'])
print(student_info['age'])
print(student_info['major'])
print(student_info['gpa'])
print(student_info['is_on'])

# modifying the dictionary
student_info['age'] = 19
print(f'updated age: {student_info["age"]}')

# dictionary methods (keys, values, items)
# .keys() returns just the keys from a dictionary.
# .values() returns just the values.
# .items() returns a list of the key-value pairs as tuples.
print('keys:', student_info.keys())
print('values:', student_info.values())
print('items:', student_info.items())