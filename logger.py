from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()

    while var < 1 or var > 2:
        var = int(input("Ошибка! Ваш выбор: "))

    var = int(input(f'\nВ каком формате записать данные?\n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'\nВаш выбор: '
                    ))
    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open("data_second_variant.csv", "a", encoding="utf-8") as file:
            file.write(f'\n{name};{surname};{phone};{adress}')



def print_data():
    print("1 файл: ")
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            print(i, end="")

    print("2 файл: ")
    with open("data_second_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            if i != '\n':
                print(i, end="")


def change_data():
    var = int(input("Введите номер файла, который Вы хотите отредактировать: "))
    name = input("Введите имя контакта, который Вы хотите отредактировать: ") 
    surname = input("Введите фамилию контакта, который Вы хотите отредактировать: ") 
    
    while var < 1 or var > 2:
        var = int(input("Ошибка! Ваш выбор: "))
   
    if var == 1:
        name_cor = input("Введите новое имя: ") 
        surname_cor = input("Введите новую фамилию: ") 
        phone_cor = input("Введите новый телефон: ") 
        adress_cor = input("Введите новый адрес: ") 

        list_3 = [name_cor, surname_cor, phone_cor, adress_cor]

        with open("data_first_variant.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
            for i in range(4, len(data)-1):
                if data[i-4].startswith(name) and data[i-3].startswith(surname): 
                    data.pop(i-1)
                    data[i-2] = str(list_3[3])+'\n'
                    data[i-3] = str(list_3[2])+'\n'
                    data[i-4] = str(list_3[1])+'\n'
                    data[i-5] = '\n'+str(list_3[0])+'\n'
            
        with open("data_first_variant.csv", "w", encoding="utf-8") as file:            
            file.write(''.join(data))    

    if var == 2:
        name_cor = input("Введите новое имя: ") 
        surname_cor = input("Введите новую фамилию: ") 
        phone_cor = input("Введите новый телефон: ") 
        adress_cor = input("Введите новый адрес: ") 

        list_3 = [name_cor,";",surname_cor,";",phone_cor,";",adress_cor,'\n']

        with open("data_second_variant.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
            # print(data)
            for i in range(0, len(data)-1):
                list_2 = (data[i]).split(";")
                # print(list_2)
                for j in range(3, len(list_2)):
                    if list_2[j-3] == name and list_2[j-2] == surname:
                        data[i] = ''.join(list_3)
                        
                        break

        with open("data_second_variant.csv", "w", encoding="utf-8") as file:            
            file.write(''.join(data))  



def delete_data():
    var = int(input("Введите номер файла, из которого Вы хотите удалить запись: "))
    name_del = input("Введите имя контакта, который Вы хотите удалить: ")
    surname_del = input("Введите фамилию контакта, который Вы хотите удалить: ")
    
    while var < 1 or var > 2:
        var = int(input("Ошибка! Ваш выбор: "))

    if var == 1:
        with open("data_first_variant.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
            for i in range(4, len(data)-1):
                if data[i-4].startswith(name_del) and data[i-3].startswith(surname_del): 
                    data.pop(i-1)
                    data.pop(i-2)
                    data.pop(i-3)
                    data.pop(i-4) 
                    data.pop(i-5)       
            
        with open("data_first_variant.csv", "w", encoding="utf-8") as file:            
            file.write(''.join(data))
    else:
        with open("data_second_variant.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
            for i in data:
                list_2 = i.split(";")
                # print(list_2)
                for j in range(1, len(list_2)-1):
                    if list_2[j-1] == name_del and list_2[j] == surname_del:
                        data.remove(i)
                        
                        break
        with open("data_second_variant.csv", "w", encoding="utf-8") as file:            
            file.write(''.join(data))
