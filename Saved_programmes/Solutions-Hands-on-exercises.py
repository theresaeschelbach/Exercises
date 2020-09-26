#!/usr/bin/env python
# coding: utf-8

# # Solutions to Hands-on Exercises
# 
# #### Please note that the solutions for various questions are individually worked out here, but several answers were combined together
# 

# In[1]:


# Employee Class
class Employee(object):
    """
    Class Employee.
    """
    
    # The class keeps a list of positions
    positions = ["Junior", "Senior", "Lead", "Assistant Manager"]

    # The initialization function that creates the Employee instance/object 
    def __init__(self, salary):
        # Create the Employee instance with salary provided during initialization
        self.salary = salary
        # Every employee starts at the junior level 
        self.position = self.positions[0]

    # A function that promotes the employee to a higher position 
    def promote(self):
        # Get the current index of the position 
        cur_position_index = self.positions.index(self.position)
        # Change the position of the employee to one higher 
        self.position = self.positions[cur_position_index + 1] 

    # A function that increases the employee's salary by 10 %
    def give_raise(self):
        self.salary += 0.1*self.salary


# In[2]:


# SOLUTIONS ARE BELOW

#=========== Question 1 ===========
# 1.
e1 = Employee(10000)
e2 = Employee(25000)
# 2.
e1.promote()
e2.promote()
e2.promote()
#e2.promote()
#e2.promote()
e1.give_raise()
e2.give_raise()
print("Salary of first employee is: ",e1.salary, " and the salary of the second employee is: ", e2.salary)
# 3. There are only a total of 4 positions, promoting an employee above 3 times causes
# us to access a value not there in the list. Hence we get an index error.
#=========== End of Question 1 ===========


# ## Revised Employee Class

# In[3]:



# Employee Class
class Employee (object):
    """
    
    """
    # The class keeps a list of positions
    positions = ["Junior", "Senior", "Lead", "Assistant Manager"]

    # The initialization function that creates the Employee instance/object 
    # Solution to question 2 and 3, adding name and ID to initializaition function
    def __init__(self, salary, name, ID):
        # Create the Employee instance with salary provided during initialization
        self.salary = salary
        self.name = name
        # Solution to Question 3:
        # Creating an ID value will not solve the problem of non-unqiue employee identification
        # Since even now, we can create 2 employees with the same ID value.
        self.ID = ID
        # Every employee starts at the junior level 
        self.position = self.positions[0]

   # A function that promotes the employee to a higher position 
    def promote(self):
        # Get the current index of the position 
        cur_position_index = self.positions.index(self.position)
        # Change the position of the employee to one higher 
        self.position = self.positions[cur_position_index + 1] 
        # Solution to to question 4
        self.give_raise()

    # A function that increases the employee's salary by 10 %
    def give_raise(self):
        self.salary += 0.1*self.salary

    # Solution to Question 5
    def demote(self):
        cur_position_index = self.positions.index(self.position)
        self.position = self.positions[cur_position_index - 1]

    # Solution to Question 6
    def reset(self, new_salary):
        self.salary = new_salary

    # Solution to Question 7

    def __str__(self):
        return "The employee's name is " + self.name + " and he earns " + str(self.salary) + " as a " + self.position
    


# ## Revised Manager Class

# In[4]:


# Manager Class 
class Manager (object):
    """
    
    """
    positions = ["Manager", "Department Head", "Director", "Higher Executive"]

    def __init__(self, salary, position):
        self.salary = salary
        self.position = position
        # We initialize the manager class with an empty list of employees under him/her
        self.employees = []

    # A function that adds an employee to the manager  
    def add_employee(self,employee):
        self.employees.append(employee)

    # Solution to Question 8.2
    def remove_employee(self, employee):
        self.employees.remove(employee)

    # Solution to Question 9
    def add_all(self, lst):
        for employee in lst:
            self.add_employee(employee)

    # Solution to Question 10
    def remove_employees(self, lst):
        for employee in lst:
            self.remove_employee(employee)    

    # Solution to Question 10 cont.
    def clear_employees(self):
        self.employees = [] 

    def __str__(self):
        return "The Manager's name is " + self.name + " and he earns " + str(self.salary) + " as a " + self.position
    


# In[5]:


#=========== Question 8.1 ===========

e1 = Employee(100, "Richard Bezos", 51)
e1.promote()
print(e1.salary)
print(e1.position)
e1.demote()
print(e1.position)
e1.reset(500)
print(e1.salary)
print(str(e1))
e2 = Employee(100, "what", 4)

m1 = Manager(500, "Manager")
m1.add_employee(e1)

print('\n'.join(str(e) for e in m1.employees))

m1.remove_employee(e1)

print('\n'.join(str(e) for e in m1.employees))

m1.add_all([e1,e2])

print('\n'.join(str(e) for e in m1.employees))

# m1.remove_employees([e1, e2])
m1.clear_employees()

print('\n'.join(str(e) for e in m1.employees))


# # Inheritence solution (Question 11)

# In[6]:


from abc import ABC, abstractmethod

class Person (ABC):
    """
    Class Person..
    """
    def __init__(self, name, salary, Id):
        if type(salary) is not int:
            # Question 14
            raise ValueError('salary is should be integer value!')
        if salary > 100000:
            # Question 14
            raise ValueError('salary can not exceed 100000 (unless you are a data scientist)!')
        
        self.salary = salary
        self.name = name
        self.Id = Id

    @abstractmethod
    def promote(self):
        pass

    @abstractmethod
    def give_raise(self):
        self.salary += 0.1*self.salary


    


# In[7]:


class Employee (Person):
    """
    Employee Inherits Person
    """
    # The class keeps a list of positions
    positions = ["Junior", "Senior", "Lead", "Assistant Manager"]

    def __init__(self, name, salary, Id, position):
        Person.__init__(self, name, salary, Id)
        if position < len(self.positions):
            self.position = position
        else:
            self.position = 0         
        #Question 16
        if position == 0 and salary > 10000:
            raise ValueError('Junior salaries may not not exceed 10000!')
        if position == 1 and salary > 20000:
            raise ValueError('Senior salaries may not not exceed 20000!')
        if position == 2 and salary > 50000:
            raise ValueError('Lead salaries may not not exceed 50000!')
        if position == 3 and salary > 100000:
            raise ValueError('Assistant Manager salaries may not not exceed 100000!')
        
    def get_employee_position(self):
        return self.positions[self.position]
    
    def promote(self):
        if self.position < len(self.positions) - 1:
            self.position += 1
            self.give_raise()
        else :
            # Question 12
            raise Exception(' The employee can not be promoted more than Assistant Manager')
            
    def give_raise(self):
        self.salary += 0.1*self.salary

    def __str__(self):
        return "The employee's name is " + self.name + " and he earns " + str(self.salary)             + " as a " + self.get_employee_position()



        

    


# In[8]:


class Manager (Person):
    """
    Manager class inherits the Person class
    """

    positions = ["Manager", "Department Head", "Director", "Higher Executive"]
    
    def __init__(self, name, salary, Id, position):
        Person.__init__(self, name, salary, Id)
        self.employees = []
        if position < len(self.positions):
            self.position = position
        else:
            self.position = 0


    def get_manager_position(self):
        return self.positions[self.position]


    def promote(self):
        if self.position < len(self.positions) - 1:
            self.position += 1
            self.give_raise()
        else :
            raise Exception(' The employee can not be propmoted more than Higher Executive')
            
    def give_raise(self):
        self.salary += 0.2*self.salary

    # solution to question no:13
    def add_employee(self,employee):
        for emp in self.employees:
            if emp.Id == employee.Id:
                #Question 13
                raise Exception('The employee with given Id already exists in the employees list!')
        self.employees.append(employee)
        

    # Solution to Question 8
    def remove_employee(self, employee):
        self.employees.remove(employee)

    # Solution to Question 9
    def add_all(self, lst):
        for employee in lst:
            self.add_employee(employee)

    # Solution to Question 10
    def remove_employees(self, lst):
        for employee in lst:
            self.remove_employee(employee)    

    # Solution to Question 10 cont.
    def clear_employees(self):
        self.employees = [] 

    def __str__(self):
        return "The Mangers's name is " + self.name + " and he earns " + str(self.salary) +         " as a " + self.get_manager_position()         + ". His employees are: \n" + ' \n'.join(str(e) for e in self.employees)          

    



# In[9]:


e1 = Employee('Charley',3800,5, 0)

print(e1.salary)
e1.promote()
e1.promote()
e1.promote()
#e1.promote() #Test promotion errorhandling
print(e1.get_employee_position())
print(e1.salary)

m1 = Manager('Tom Harris ',60000, 14, 1)

e2 = Employee('Alice', 3600, 7 ,0)

#e3 = Employee('Bob', '47000', 9 ,0)
#e3 = Employee('Bob', 147000, 9 ,0)
e3 = Employee('Bob', 9000, 9 ,0)
e3.promote()
e3.promote()

m1.add_all([e1, e2, e3])

e4 = Employee('Alice', 3600, 11 ,0)

m1.add_employee(e1)

print(m1)

