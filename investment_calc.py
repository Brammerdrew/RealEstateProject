class RentalProperty:
    def __init__(self, purchase_price, down_payment, closing_costs, rehab_budget, monthly_rent, mortgage_rate, mortgage_term, vacancy,
                 property_tax, property_management, insurance, maintenance, cap_ex, rental_income,
                 laundry_income, storage_income, misc_income, mortgage_payment):
        self.purchase_price = purchase_price
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.monthly_rent = monthly_rent
        self.mortgage_rate = mortgage_rate
        self.mortgage_term = mortgage_term
        self.vacancy = vacancy
        self.property_tax = property_tax
        self.property_management = property_management
        self.insurance = insurance
        self.maintenance = maintenance
        self.cap_ex = cap_ex
        self.rental_income = rental_income
        self.laundry_income = laundry_income
        self.storage_income = storage_income
        self.misc_income = misc_income
        self.mortgage_payment = mortgage_payment

    def monthly_expenses(self):
        return self.property_tax + self.property_management + self.insurance + self.maintenance + self.cap_ex + self.mortgage_payment

    def monthly_income(self):
        return self.rental_income + self.laundry_income + self.storage_income + self.misc_income

    def upfront_costs(self):
        return self.purchase_price + self.down_payment + self.closing_costs + self.rehab_budget

    def yearly_income(self):
        return self.monthly_income() * 12

    def yearly_expenses(self):
        return self.monthly_expenses() * 12

    def cash_flow(self):
        return self.yearly_income() - self.yearly_expenses()

    def calculate_roi(self):
        return (self.cash_flow() / self.upfront_costs()) * 100  # Return ROI as a percentage


def main():
    purchase_price = float(input("What is the purchase price? "))
    down_payment = float(input("What is the down payment? "))
    closing_costs = float(input("What are the closing costs? "))
    rehab_budget = float(input("What is the rehab budget? "))
    monthly_rent = float(input("What is the monthly rent? "))
    mortgage_rate = float(input("What is the mortgage rate? "))
    mortgage_term = float(input("What is the mortgage term? "))
    vacancy = float(input("What is the vacancy rate? "))
    property_tax = float(input("What is the property tax? "))
    property_management = float(input("What is the property management fee? "))
    insurance = float(input("What is the insurance cost? "))
    maintenance = float(input("What is the maintenance cost? "))
    cap_ex = float(input("What is the capital expenditure cost? "))
    rental_income = float(input("What is the rental income? "))
    laundry_income = float(input("What is the laundry income? "))
    storage_income = float(input("What is the storage income? "))
    misc_income = float(input("What is the misc income? "))
    mortgage_payment = float(input("What is the mortgage payment? ")) 

    rental_property = RentalProperty(
        purchase_price, down_payment, closing_costs, rehab_budget, monthly_rent, mortgage_rate, mortgage_term, vacancy,
        property_tax, property_management, insurance, maintenance, cap_ex, rental_income,
        laundry_income, storage_income, misc_income, mortgage_payment
    )

    print("The monthly expenses are: ${:.2f}".format(rental_property.monthly_expenses()))
    print("The monthly income is: ${:.2f}".format(rental_property.monthly_income()))
    print("The upfront costs are: ${:.2f}".format(rental_property.upfront_costs()))
    print("The yearly income is: ${:.2f}".format(rental_property.yearly_income()))
    print("The yearly expenses are: ${:.2f}".format(rental_property.yearly_expenses()))
    print("The cash flow is: ${:.2f}".format(rental_property.cash_flow()))
    print("The ROI is: {:.2f}%".format(rental_property.calculate_roi()))


if __name__ == "__main__":
    main()


        



        
