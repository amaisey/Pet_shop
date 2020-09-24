# Andrew Maisey, Benjamin Richardson, Sam Hansen, Sarah Anderson
# OOP Pet Shop Assignment for IS 403

# Write a program that prompts the user to enter in the number of customers for your Pet Boarding company. You
# do NOT need to store each customer in a list since we haven't talked about that yet. However, you need to
# implement this using classes.


# Customer Class:
    # Instance variables:
        # cust_id of type string
        # first_name of type string
        # last_name of type string
        # sAddress1 of type string
        # sAddress2 of type string
        # sCity of type string
        # sState of type string
        # zip of type string
        # fBalance of type float (How much they owe)
        # cust_pet of type Pet (In a class diagram when the arrow from the pet class points to the
        # Customer class that indicates that a Customer object "has a" Pet object. So you will need to include
            # cust_pet (or some name that you want to use) so that the Customer object can hold a pet object. 
            # Since there is just an arrow it indicates it is a one to one relationship. 
            # In IS 401 you will see that you can include multiplicity to indicates the number relationship (0 to 1, 1 to 1, 1 to many, many to many, etc.).
    # Methods:
        # Constructor should:
            # receives first_name, last_name, sAddress1, sAddress2, sCity, sState, and zip and store
            # those values to associated instance variables
            # initialize fBalance to 0.0
            # initialize the cust_pet to None
            # calculate the cust_id by calling gen_id method passing first_name, last_name, and
                # sAddress1. Make sure there are no trailing or leading spaces in the passed values.
                
        # gen_id() receives the first_name, last_name, sAddress1 and takes the first 3 letters from
        
            # the first name, first 3 letters from the last name, and first 5 letters from the address 
            # to create the cust_id and returns that string value which when called will be assigned back to the cust_id attribute in the Customer class
            # Replace any spaces in the string with no space ('')
            # note: In the program, do not prompt the user to ever enter the cust_id. It is generated
                # from the logic above.
        # return_bill() will return the following string (not print):
            # If the user entered greg for the first name and anderson for the last name and
            # 2677 east 1000 south for the sAddress1, the output would be:
            # Customer greand2677e with name greg anderson owes $123.50 for charlie's stay from 10/01/2020 to 10/20/2020
            # Where greg is the first_name, anderson is the last_name, 123.50 is the fBalance, charlie is the pet, 10/01/2020 is the begin date, and 10/20/2020 is the end date
        # make_payment() should receive a float value and subtract the amount from the fBalance
        # attribute and update the fBalance attribute o ClassVariable:
        #  company_name is of type string with the value of Critter Watch



class Customer:
    sCompanyName = "Critter Watch"
    sCustId = ""

    def __init__(self, sFName, sLName, sAddress1, sAddress2, sCity, sState, sZip):
        self.sFName = sFName
        self.sLName = sLName
        self.sAddress1 = sAddress1
        self.sAddress2 = sAddress2
        self.sCity = sCity
        self.sState = sState
        self.sZip = sZip
        self.fBalance = 0.0
        self.sCustPet = None
        self.sCustID = gen_id(sFName, sLName, sAddress1)
        
    def gen_id(self, sFName, sLName, sAddress1):
        sCustID = sFName[:3] + sLName[:3] + sAddress1[:5]
        return(sCustID)

    def return_bill(self):
        return ("Customer " + self.sCustID + " with name " + self.sFName + " " + self.sLName + " owes $" + self.fBalance + " for " + self.sCustPet.sPetName + 
                " from " + self.sCustPet.oAppointment.iBeginDate + " to " + self.sCustPet.oAppointment.iEndDate)

    def make_payment(self, fPayment):
        self.fBalance = self.fBalance - fPayment
        


# Pet Class
# Instance Variables:
    # sPetName is of type string
    # sBreed is of type string
    # iAge is of type int
    # appointment of type Appointment
    # When calling the Appointment constructor you will want to pass the owner
        # (Customer object) which is received when the Pet constructor is called:
        # oCustomer.cust_pet = Pet(sPet_Name, sBreed, iAge, oCustomer)
# Method
    # Constructor that receives sPetName, sBreed, iAge, and owner (variable that holds the
    # customer object)
        # owner will be the customer object
    # note: When creating the Appointment object and assigning to the appointment attribute
        # in the Pet constructor, pass the owner to the Appointment constructor like:
        # self.appointment = Appointment(owner)
    # This passes the variable owner which should contain the Customer object

class Pet :
    def __init__(self, sPetName, sBreed, iAge, oCustomer) :
        self.sPetName = sPetName #string
        self.sBreed = sBreed #string
        self.iAge = iAge #int
        self.oOwner = oCustomer
        self.oAppointment = Appointment(self.oOwner)
            

    
# Appointment Class
# Instance Variables:
    # iBeginDate of type date (don't worry about the time)
    # iEndDate of type date (don't worry about the time)
    # fDayRate of type float
    # iTotalDays of type int
    # iTotalCost of type float
    # owner of type owner (parameter received when calling constructor)
        # def __init__(self, owner) :
# Methods:
    # Constructor receives owner object (customer)
    # set_appointment() that receives iBeginDate, iEndDate, and fDayRate and calls the
        # calc_days() method and store the iTotalDays and calculate the iTotalCost (iTotalDays *
        # fDayRate)
    # set_appointment() updates the fBalance by calling the self.owner.fBalance which is the
        # customer object that was created and assigning it the iTotalCost
    # calc_days() calculates the iTotalDays by substracting the iEndDate from the iBeginDate.
        # However, you must return the days value for the formula:
        # self.iTotalDays = (self.iEndDate - self.iBeginDate).days
    # calc_days() should check if the iTotalDays is less than or equal 0 and if so, assign a 1 to the
        # iTotalDays
    # calc_days() should calculate the iTotalCost by multiplying iTotalDays by fDayRate

class Appointment :
    def __init__(self, oCustomer) :
        self.iTotalDays
        self.iTotalCost
        self.oOwner = oCustomer
    
    def set_appointment(self, iBeginDate, iEndDate, fDayRate) :
        self.iBeginDate = iBeginDate
        self.iEndDate = iEndDate
        self.fDayRate = fDayRate

        calc_days()

        #update fBalance by calling self.owner.fBalance (customer object) and assign it iTotalCost
        self.oOwner.fBalance = self.iTotalCost
        
    #store iTotalDays
    #iTotalCost = iTotalDays * fDayRate
    def calc_days (self):
        self.iTotalDays = (self.iEndDate - self.iBeginDate).days

        if (self.iTotalDays <= 0):
            self.iTotalDays = 1
        
        self.iTotalCost = self.iTotalDays * self.fDayRate
        
    


# Your company has some strange business practices in that a Customer can only have 1 pet. And the way your
    # program is set up, you only keep track of the latest boarding of the pet with a begin and end date and a cost per
    # day based upon the pet.
# Create the necessary classes represented in the diagram above. A customer has a pet and a pet has an
    # appointment.
# Also, the company name is Critter Watch and that should be stored as a class variable that all Customer objects
    # can access.
# Have the user input the data for the customer into variables and then call the customer constructor passing the
    # data to the constructor.
# Gather the data for the pet as variables and create the pet object and assign it to the cust_pet attribute for the
    # current customer object.
# Gather the data for the appointment as variables and call the set_appointment() method for the appointment
    # object in the cust_pet object in the customer object (Customer has a pet and the pet has an appointment).
# Print the current bill by calling the return_bill() method
# Call the make_payment() method and then print the current bill again calling the return_bill() method
# For those that want an extra 3 points on the assignment you can implement the pet attribute as a list and the
    # appointment attribute as a list.
    
# HINT:
# dBegin_Date = datetime.strptime(input("Enter Start date in the format m/d/y: "), "%m/%d/%Y")and make sure
# you use:
# from datetime import datetime.
# Otherwise if you use:
# import datetime
# then you have to use:
# dBegin_Date = datetime.datetime.strptime(input("Enter Start date in the format m/d/y: "), "%m/%d/%Y")