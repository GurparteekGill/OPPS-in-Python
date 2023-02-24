


class Employee:
    empname="Varun"
    salary="88887"
    company="Youngsman"

    # The moment an object if created the init constructor will run automatically
    def __init__(self,empname="Unknown",salary="4500",company="unknow"):
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


''' Now,For varun it will not give error because when we will create a constuctor
    it will take the default values '''
Varun=Employee()
Varun.empdetail()

print( "''''''''''''''''''")
print(Gurparteek.company)
print(Simar.company)
print(Yuvi.company)
