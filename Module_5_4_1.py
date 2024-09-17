class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    ''' Моя первая программа с комминтарием
    клас пользователя Регистрация пользователя
    Логин и пароль
    '''

    def __init__(self, username, password, password_confirmation):
        self.username = username
        if password == password_confirmation:
            # if is_password_good():
            self.password = password
    # def is_password_good(password):
    #     if len(password) < 8:
    #         return False
    #     s = password
    #     if s.upper() == password:
    #         return False
    #     s = password
    #     if s.lower() == password:
    #         return False
    #     flag = False
    #     for i in range(len(password)):
    #         if password[i] in "0123456789":
    #             flag = True
    #     if flag == False:
    #         return False
    #     else:
    #         return True



# print(User.__doc__)
if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Привет! Выберите действие: \n1 - Выход\n2 - Регистрация \n"))
        if choice == 1:
            login = input('Введите свой логин: ')
            password = input('Введите свой пароль: ')
            if login in database.data:
                print('OK')
        if choice == 2:
            user = User(input('Введите логин: '), password1 := input('Введите пароль: '),
                        password2 := input('Введите подтверждение: '))
            if password1 != password2:
                exit()
            database.add_user(user.username, user.password)
        print(database.data)