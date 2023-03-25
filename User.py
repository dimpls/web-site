class User:
    def __init__(self, user_id, email, password, name, phone_number):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.name = name
        self.phone_number = phone_number

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
