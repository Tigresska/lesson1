# nums = [1,2,3,4,5,6,7,8,9,10]
# for num in nums:
#     print(num+1)

# string = input('Введите строку:')
# for char in string:
#      print(char)

pupil_marks =[
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '3b', 'scores': [5,5,4,5,3]},
    {'school_class': '3a', 'scores': [5,5,5,5,2]},
    {'school_class': '4b', 'scores': [2,3,4,5,3]}
]
schoolresult = 0
school_marks = 0
for sh_class in pupil_marks:
    result = 0
    count_marks = 0
    for mark in sh_class['scores']:
        result += mark
    count_marks = len(sh_class['scores'])
    print(f"Класс {sh_class['school_class']} средний балл {result/count_marks}")
    schoolresult += result
    school_marks += count_marks
print(f"Средний был по школе {schoolresult/school_marks}")
