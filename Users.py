class Users():
    id = 0
    name = str
    surname = str
    login = str
    password = str
    group = str
    def Default_Users(self):
        self.id = self.id+1
        self.name="NONE"
        self.surname = "NONE"
        self.login = "NONE"
        self.password = "NONE"
        self.group = "NONE"
    def New_Users(self,n,s,l,p,g):
        self.id = self.id + 1
        self.name = n
        self.surname = s
        self.login = l
        self.password = p
        self.group = g
    def Change_Users(self,i,n,s,l,p,g):
        if self.id==i:
            self.name = n
            self.surname = s
            self.login = l
            self.password = p
            self.group = g
    def RetUsers(self,n):
        if self.name==n:
            return (f"Id: {self.id}   Name: {self.name}   Surname: {self.surname}   Login: {self.login}   Password {self.password}   Group {self.group} ")
        else:
            return "NONE"