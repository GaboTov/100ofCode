
""" numbers = [1,2,3]

new_numbers = [n+1 for n in numbers]

print(new_numbers) """


""" name = "algo"
letters = [letter for letter in name]
print(list(name))
print(letters)


number = [n *2 for n in range(1,5)]
print(number) """

""" names = ['Alex', 'Beth', 'Caroline', 'Dave','Eleanor', 'Freddie']

big_names_capitalize = [name.upper() for name in names if len(name) > 5]

print(big_names_capitalize) """

numbers = [1,1,2,3,5,8,13,21,34,55]

""" solution = [number**2  for number in numbers]
print(solution) """

""" solution = [number for number in numbers if number%2 == 0]
print(solution) """
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave','Eleanor', 'Freddie']

student_score = {student: random.randint(1,100) for student in names}
print(student_score)
passed_students = {key: value for (key,value) in student_score.items() if value > 60}
print(passed_students)