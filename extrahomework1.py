grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students1 = sorted(list(students))
dict = {}
dict[students1[0]] = sum(grades[0]) / len(grades[0])
dict[students1[1]] = sum(grades[1]) / len(grades[1])
dict[students1[2]] = sum(grades[2]) / len(grades[2])
dict[students1[3]] = sum(grades[3]) / len(grades[3])
dict[students1[4]] = sum(grades[4]) / len(grades[4])
print(dict)



