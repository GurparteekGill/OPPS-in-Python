class Employee:

    # The moment an object if created the init constructor will run automatically
    def __init__(self,empname,salary,company):
        print("Creting Employee :")
        self.empname=empname
        self.salary=salary
        self.company=company

    def empdetail(self):
        print(f"The Name of Emp is :{self.empname}")
        print(f"The salary of Emp is :{self.salary}")
        print(f"The company of Emp is :{self.company}")
        
    



Gurparteek=Employee("GURPARTEEK","5678","DUKE")
Gurparteek.empdetail()
Simar=Employee("SIMAR","45435","Google")
Simar.empdetail()
Yuvi=Employee("Yuvraj","77894","Mcd")
Yuvi.empdetail()


''' For varun it will give error because we have  not given any parameter '''
'''Varun=Employee()
Varun.empdetail()'''

print( "''''''''''''''''''")

''' This line will error because we can not use any Instance variable from
    a class in this way  '''
         # print(Gurparteek,{self.company})



print(Simar.company)
print(Yuvi.company)
