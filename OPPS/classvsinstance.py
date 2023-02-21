class Employee :
    company="Google"   #Class Atrribute 


                                          #######Note : Instance attribute take preference over class attribute.
harry= Employee()
print(harry.company)  



Employee.company="Youtube"   #Instance Attribute
print(harry.company)