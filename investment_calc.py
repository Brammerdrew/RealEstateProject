class rentalProperty:
    def __init__(self, rental_income, misc_income, piti_expenses, maintenance_expenses, misc_expenses, down_payment, rehab_costs):
        self.rental_income = rental_income
        self.misc_income = misc_income
        self.piti_expenses = piti_expenses
        self.maintenance_expenses = maintenance_expenses
        self.misc_expenses = misc_expenses
        self.down_payment = down_payment
        self.rehab_costs = rehab_costs


    def total_income(self):
        return (self.rental_income + self.misc_income) * 12
    
    def total_expenses(self):
        return (self.piti_expenses + self.maintenance_expenses + self.misc_expenses) * 12
        
    def calc_net_income(self):
        return self.total_income() - self.total_expenses()
    
    def upfront_investment(self):
        return self.rehab_costs - self.down_payment
    

class ROI:
    def __init__(self, property):
        self.property = property

    def calc_roi(self):
        net_income = self.property.calc_net_income()
        total_investment = self.property.upfront_investment()
        roi = (net_income / total_investment) * 100 
        return roi
    
test_property = rentalProperty(2400,0,1150,250,250,4500,20000)
roi_calculater = ROI(test_property)
roi = roi_calculater.calc_roi()
print(roi)


        
