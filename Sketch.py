class Sketch:
    def __int__(self, sketch_id, description, price):
        self.sketch_id = sketch_id
        self.description = description
        self.price = price

    def get_sketch_id(self):
        return self.sketch_id

    def set_sketch_id(self, sketch_id):
        self.sketch_id = sketch_id

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price