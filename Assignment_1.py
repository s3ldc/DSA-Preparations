class Employee:
    def __init__(self, empid=None, name=None, salary=None):
        self.empid = empid
        self.name = name
        self.salary = salary

    # One way to print object details
    def setEmpid(self, empid):
        self.empid = empid

    def setName(self, name):
        self.name = name

    def setSalary(self, salary):
        self.salary = salary

    def getEmpid(self):
        return self.empid
    
    def getName(self):
        return self.name
    
    def getSalary(self):
        return self.salary 
    
    # Second way to print object details
    def show(self):
        print(self.empid, self.name, self.salary)
    
e1 = Employee(1, "Naman", 90000)

e2 = Employee()
e2.setEmpid(2)
e2.setName("Ankit")
e2.setSalary(85000)

print(e1.getEmpid(), e1.getName(), e1.getSalary())
print(e2.getEmpid(), e2.getName(), e2.getSalary())

e1.show()
e2.show()