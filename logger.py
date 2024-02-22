from data_cr import name_data, surname_data, phone_data, adress_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 вариант: \n"
    f"{name}\n{surname}\n{phone}\n{adress}\n\n"
    f"2 вариант: \n"
    f"{name};{surname};{phone};{adress}\n"
    f"Выберите вариант: "))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    if var == 1:
        with open('data_fr.csv', 'a') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{adress}\n\n")
    elif var == 2:
        with open('data_sec.csv', 'a') as f:
            f.write(f"{name};{surname};{phone};{adress}\n")

def print_data():
    print('Вывожу данные из первого файла: \n')
    with open('data_fr.csv', 'r') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range (len(data_first)):
            if data_first[i] == "\n" or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))


    print('Вывожу данные из второго файла: \n')
    with open('data_sec.csv', 'r') as f:
        data_second = f.readlines()
        print(*data_second)

input_data()
print_data()