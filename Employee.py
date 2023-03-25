class Employee:

    def __int__(self, employee_id, name, phone_number, work_experience, email, password, position):
        self.employee_id = employee_id
        self.name = name
        self.phone_number = phone_number
        self.work_experience = work_experience
        self.email = email
        self.password = password
        self.position = position

    def get_employee_id(self):
        return self.employee_id

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_work_experience(self):
        return self.work_experience

    def set_work_experience(self, work_experience):
        self.work_experience = work_experience

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position