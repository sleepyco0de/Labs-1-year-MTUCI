class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        print("Пароль успешно изменён.")

    def check_password(self, password):
        return self.__password == password


if __name__ == "__main__":
    user = UserAccount("user123", "user@example.com", "password123")
    print(user.check_password("password123"))  # True
    print(user.check_password("wrongpassword"))  # False
    user.set_password("newpassword123")
    print(user.check_password("newpassword123"))  # True
    print(user.check_password("password123"))  # False
