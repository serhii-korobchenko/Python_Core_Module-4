""" Второй этап. Необходимо написать функцию is_valid_password, 
которая будет проверять полученный параметр — пароль на надежность.

Критерии надежного пароля:

1)Длина строки пароля восемь символов.
2) Содержит хотя бы одну букву в верхнем регистре.
3)Содержит хотя бы одну букву в нижнем регистре.
4)Содержит хотя бы одну цифру.

Функция is_valid_password должна вернуть True, если переданный в 
качестве параметра пароль отвечает требованиям надежности. 
В противном случае вернуть False. """

def is_valid_password(password):
    flag = 0
    if len(password) == 8:
        if password.islower() == False:
            if password.isupper() == False:
                for item in password:
                    if item.isdigit():
                        flag = 1
    if flag == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_valid_password("Bbcec333")) # True
    #print(is_valid_password("z,qrE*IE")) # True