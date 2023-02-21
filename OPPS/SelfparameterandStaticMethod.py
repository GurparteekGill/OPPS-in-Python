class Employee:
    company="Youngsman"
    salary=7500

    '''With the help of self parameter yopu can use the Instance attributes of that particular class. IF Instance attribute of that particular class
      is not given ,then it will use the class attributes ,like in the case of Varun '''  
    def getsalary(self,signature):
        print(f"Salary of Employee working in company  {self.company} is  :{self.salary} \n{signature}")
       

    ''' Sometime you need a function that does nothing  is Known as Static Method or Function'''
    @ staticmethod
    def Greet ():
        print("Welcome Sir Ji")

Gurparteek=Employee()
Simar=Employee()
Yuvi=Employee()
Varun=Employee()

Gurparteek.company="Duke" #Instance variable of Gurparteek Object
Simar.company="Sony"      #Instance variable of Simar Object
Yuvi.company="Mcd"        #Instance variable of Yuvi Object

Gurparteek.salary=3456    #Instance variable of Gurparteek Object
Yuvi.salary=9999          #Instance variable of Simar Object
Simar.salary=4574         #Instance variable of Yuvi Object

Gurparteek.getsalary("GSP76")
Gurparteek.Greet()
Simar.getsalary("SSP56")
Gurparteek.Greet()
Yuvi.getsalary("YUJ90")
Gurparteek.Greet()
Varun.getsalary("VV56T") 
Gurparteek.Greet()




