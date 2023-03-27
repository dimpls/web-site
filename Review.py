class Review:

    def __init__(self, review_id, user_id, employee_id, body):
        self.review_id = review_id
        self.user_id = user_id
        self.employee_id = employee_id
        self.body = body

    def get_review_id(self):
        return self.review_id

    def set_review_id(self, review_id):
        self.review_id = review_id

    def get_author_id(self):
        return self.author_id

    def set_author_id(self, author_id):
        self.author_id = author_id

    def get_employee_id(self):
        return self.employee_id

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def get_body(self):
        return self.body

    def set_body(self, body):
        self.body = body