class stud:
    def setid(self, id):
        self.id = id

    def getid(self):
        return self.id

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setaddress(self, add):
        self.address = add

    def getaddress(self):
        return self.address

    def setmarks(self, marks):
        self.marks = marks  # Fix: Assign marks to self.marks

    def getmarks(self):
        return self.marks  # Added this getter method for marks
