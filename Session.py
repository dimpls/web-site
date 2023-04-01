from User import User
from Employee import Employee


class Session:
    def __init__(self, session_id, user_id, date, description, status, employee_id, sketch_id):
        self.session_id = session_id
        self.user_id = user_id
        self.date = date
        self.description = description
        self.status = status
        self.employee_id = employee_id
        self.sketch_id = sketch_id

    def get_user_instance(self):
        usr = User(self.user_id.user_id, self.user_id.email, self.user_id.password, self.user_id.name,
                   self.user_id.phone_number)
        lst_user = [usr.user_id, usr.email, usr.password, usr.name, usr.phone_number]
        return lst_user

    def set_user_instance(self, user_id):
        if isinstance(user_id, User):
            self.user_id = user_id
        else:
            raise ValueError("[ERROR]User should be an instance of User class")

    def get_session_id(self):
        return self.session_id

    def set_session_id(self, session_id):
        self.session_id = session_id

    def get_employee_instance(self):
        emp = Employee(self.employee_id.employee_id, self.employee_id.name, self.employee_id.email,
                       self.employee_id.password, self.employee_id.phone_number, self.employee_id.work_experience,
                       self.employee_id.position)
        lst_emp = [emp.employee_id, emp.name, emp.email, emp.password, emp.phone_number, emp.work_experience,
                   emp.position]
        return lst_emp

    def set_employee_instance(self, employee_id):
        if isinstance(employee_id, Employee):
            self.employee_id = employee_id
        else:
            raise ValueError("[ERROR]Employee should be an instance of Employee class")

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_sketch_id(self):
        return self.sketch_id

    def set_sketch_id(self, sketch_id):
        self.sketch_id = sketch_id
