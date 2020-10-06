""" user_info = {'first_name' : 'Anastasiia', 'last_name' : 'Okataia'}

print(user_info['last_name'])

my_list = [3,5,7,9,10.5]
print(my_list)
my_list.append('Python')
print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[-1])
print(my_list[1:5])
my_list.remove('Python')
print(my_list)
 """
new_dict = {'city': 'Москва', 'tempreture': '20'}
print(new_dict['city'])
new_dict['tempreture'] = str(int(new_dict['tempreture']) - 5)
print(new_dict)
print(new_dict.get('country', 'Россия'))
new_dict['date'] = '27.05.2019'
print(len(new_dict))