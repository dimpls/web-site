class Session:
    def __init__(self, session_id, user_id, date, description, status, employee_id, sketch_id):
        self.session_id = session_id
        self.user_id = user_id
        self.date = date
        self.description = description
        self.status = status
        self.employee_id = employee_id
        self.sketch_id = sketch_id

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_session_id(self):
        return self.session_id

    def set_session_id(self, session_id):
        self.session_id = session_id

    def get_eployee_id(self):
        return self.eployee_id

    def set_eployee_id(self, eployee_id):
        self.eployee_id = eployee_id

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