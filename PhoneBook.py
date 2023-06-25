import os

file_name = "Phone.txt"
my_file = open (file_name, "a+")
my_file.close()

def main_menu():
    print ("\nМеню\n")
    print ("1. Просмотр контактов")
    print ("2. Создание контакта")
    print ("3. Поиск контакта по телефону")
    print ("4. Поиск телефона по Фамилии")
    print ("5. Редакция контакта")
    print ("6. Удаление контакта")
    print ("7. Выход")

    сhoose = input("\nВведите № действия: ")
    if сhoose == "1":
        all_contact()
        enter = input ("Нажмите Enter")
        main_menu()
    elif сhoose == "2":
        new_contact()
        enter = input ("Нажмите Enter")
        main_menu()
    elif сhoose == "3":
        find_contact ()
        enter = input ("Нажмите Enter")
        main_menu()
    elif сhoose == "4":
        find_phone()
        enter = input ("Нажмите Enter")
        main_menu()
    elif сhoose == "5":
        redactor_contact()
        enter = input ("Нажмите Enter")
        main_menu()
    elif сhoose == "6":
        delete_contact()
        enter = input ("Нажмите Enter")
        main_menu()
    elif сhoose == "7":
        print ("Пока")
    else: 
        print ("Не ввели № действия!")
        enter = input ("Нажмите Enter")
        main_menu()
    
def all_contact():
    my_file = open(file_name, "r")
    data = my_file.read()
    if len (data) > 0: print (data)
    else: print ("Нет контактов")
    my_file.close()

def new_contact():
    second_name = input ("Введите фамилию: ")
    second_name = proverka(second_name)
    name = input ("Введите имя: ")
    name = proverka(name)
    phone = input ("Введите телефон: ")
    phone = proverka (phone)
    emailID = input ("Введите почту: ")
    status = input ("Группа контакта: ")
    contact = second_name + " " + name + " " +  phone + " " +  emailID + " " +  status + "\n"
    my_file = open (file_name, "a+")
    my_file.writelines (contact)
    my_file.close()
    print ("\nСоздан новый контакт")

def proverka (word):
    while len(word) == 0:
        print ("Не ввели данные!")
        word = input ("Введите повторно данные: ")
    return (word.title())

def find_contact ():
    count = 0
    f_phone = input ("Введите телефон для поиска: ")
    my_file = open (file_name, 'r')
    lines = my_file.readlines()
    for line in lines:
        if f_phone in line: 
            count += 1
            print (line)
    my_file.close()
    if count == 0: print ("Нет такого контакта")

def find_phone():
    count = 0
    f_second_name = input ("Введите фамилию для поиска: ")
    my_file = open (file_name, "r")
    lines = my_file.readlines()
    for line in lines:
        if f_second_name in line:
            line = line.split()
            print (line[2])
            count += 1
    my_file.close()
    if count == 0: print ("Нет такого контакта")

def redactor_contact():
    test = "Test.txt"
    f_phone = input ("Введите телефон для поиска: ")
    new_phone = input ("Введите новый телефон: ")
    with open(file_name) as my_file, open(test, "w") as test_file:
        for line in my_file:
            if f_phone not in line:
                test_file.write(line)
            else: 
                line = line.split()
                line [2] = new_phone
                line = " ".join(line)
                test_file.write(line)
    
    os.remove(file_name)
    os.rename(test, file_name)

def delete_contact():
    test = "Test.txt"
    f_phone = input ("Введите телефон для поиска: ")
    with open (file_name) as my_file, open (test, "w") as dop_test:  
        for line in my_file:
            if f_phone not in line:
                dop_test.write(line)
    os.remove(file_name)
    os.rename(test, file_name)


main_menu()