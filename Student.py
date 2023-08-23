import pandas as pd
import numpy as np

def compare_students(student1, student2):
    criteria_match_count = np.sum(student1 == student2)
    return criteria_match_count > 3

def find_similar_students(data):
    similar_students = []
    for i, student1 in data.iterrows():
        for j, student2 in data.iterrows():
            if i != j and student1['Name'] == student2['Name']:
                student1_data = student1.values[1:]  # Exclude the 'Name' column
                student2_data = student2.values[1:]  # Exclude the 'Name' column
                if compare_students(student1_data, student2_data):
                    similar_students.append(student1['Name'])
                    break
    return similar_students

# Load the CSV data into a pandas DataFrame
csv_file = 'student_data.csv'
data = pd.read_csv(csv_file)

# Find students with more than three similar criteria
similar_students = find_similar_students(data)

# Print the names of similar students
print("Students with more than 3 similar criteria:")
for student_name in similar_students:
    print(student_name)
