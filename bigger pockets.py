
class Investment():
    def __init__(self,rental_income):
        self.rental_income= rental_income
 
         

    def Income (self,):
        self.rental_income = int(input('What is your rental income?'))
        self.laundary=int(input('What is your laundry income?'))
        self.storage=int(input('What is your storage income?'))

        if self.rental_income>0:
            print({'your rental income is{self.rental_income}'})
        if self.laundary>0:
            print({'your laundary is{self.laundary}'})    
        if self.storage>0:
            print({'your storage is{self.storage}'})
        else:  
          
          print("your input is invalid." )


      

     
    def expenses(self,):
        self.tax=int(input('How much is your tax?'))
        self.Insurance= int(input('How much is your insurance?'))
        self.Utilities=int(input('How much is your Utilities?'))
        self.HOA=int(input('How much is your HOA fees?'))
        self.Vacancy=int(input('How much is your vacancy?'))
        self.Repairs=int(input('How much are your Repairs?'))
        self.Capex=int(input('How much is your capex?'))
        self.property_managment=int(input('How much is your property management?'))
        self.mortgage= int(input('How much is your mortgage?'))

        
        if self.tax>= 0:
            print(f"Your monthly taxes is {self.tax}")
        if self.Insurance >= 0:
            print(f"Your monthly insurance is {self.Insurance}")  
        if self.Utilities >= 0:
            print(f"Your monthly Utilities is {self.Utilities}")
        if self.HOA>= 0:
            print(f"Your monthly insurance is {self.HOA}")
        if self.Vacancy >= 0:
            print(f"Your monthly vacancy is {self.Vacancy}")
        if self.Repairs >= 0:
            print(f"Your monthly repair is {self. Repairs}")
        if self.Capex >= 0:
            print(f"Your monthly Capex is {self.Capex}")
        if self.property_managment >= 0:
            print(f"Your monthly property management fee is {self.property_managment}")
        if self.mortgage >= 0:
            print(f"Your monthly mortgage is {self.mortgage}")
        else:
             print("your input is invalid." )


    def cash_flow (self,cash_flow):
        self.cash_flow=cash_flow

        self.total_monthly_cash_flow = self.total_monthly_income - self.total_monthly_expenses
        print(f"The total monthly cash flow is {self.total_monthly_cash_flow}")

        self.total_annual_cash_flow = self.total_monthly_cash_flow * 12
        print(f"The total annual cash flow is {self.total_annual_cash_flow}")


    def cash_on_cash_ROI(self,):
         self.closing_costs=int(input('How much is your closing costs?'))
         self.Repair_money=int(input('How much is your Repair money?'))
         self.monthly_income=int(input('How much is your monthly income?'))
         self. down_payment= int(input('How much is your down payment?'))

    def run(self):
         while True:
            response = str(input("Would you like to calculate your ROI? Yes, No")).lower()
            if response == "Yes":
                self.income()
                self.expenses()
                self.cashflow()
                self.investment()
            elif response == "No":
                print("Have a good day")
                return
            else:
                print("Invalid input, please try again.")
   

     


   

  
    
    
    
   

   
      