def age_prof(age):
    if age < 7:
        return 'учиться в детском саду'
    elif 7<= age and age <= 18:
        return 'учиться в школе'
    elif 18<age and age <= 23:
        return 'учиться в ВУЗе'
    elif age > 23:
        return 'работать'

def str_equal(string1, string2):
    if type(string1) == str and type(string2) == str:
        if string1 == string2:
            return 1
        elif len(string1) > len(string2):
            return 2
        elif string2 == 'learn':
            return 3
    else:
        return 0

print(str_equal('fgjh', 'learn'))

# age = int(input('Введите ваш возраст: '))
# prof = age_prof(age)
# print(prof)

