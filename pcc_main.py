# Employee class that holds employee and dependents along with pay information
class Employee:
    # Defined as the employee name and an array of dependent names
    def __init__(self, name=None, dependents=None, pay_paycheck=2000.0, paychecks_year=26):
        if dependents is None:
            dependents = []
        self.employee_name = name
        self.dependents = dependents
        self.pay_paycheck = pay_paycheck
        self.paychecks_year = paychecks_year

    # Set employee to blank
    def reset_employee(self):
        self.clr_dependents()
        self.clr_employee()

    # Check if dependents is empty
    def no_dependents(self):
        if len(self.dependents) == 0:
            return True
        else:
            return False

    # Set dependents of employee
    def set_dependents(self, dependents):
        self.dependents = dependents
        return

    # Add dependent to employee
    def add_dependent(self, dependent):
        self.dependents.append(dependent)
        return

    # Remove dependent from employee
    def del_dependent(self, dependent):
        self.dependents.remove(dependent)
        return

    # Clear all dependents from employee
    def clr_dependents(self):
        self.dependents = []
        return

    # Return list of dependents (names) associated with the employee
    def get_dependents(self):
        return self.dependents

    # Set employee name
    def set_employee(self, name):
        self.employee_name = name
        return

    # Remove employee name
    def clr_employee(self):
        self.employee_name = None
        return

    # Get employee name
    def get_employee(self):
        return self.employee_name


# Benefits class that holds standard benefits cost and any discount information for calculations
class Benefits:
    def __init__(self, discount_letter='a', discount_amount=0.10, employee_benefit_cost_year=1000.0, dependent_benefit_cost_year=500.0):
        self.discount_letter = discount_letter
        self.discount_amount = discount_amount
        self.employee_benefit_cost_year = employee_benefit_cost_year
        self.dependent_benefit_cost_year = dependent_benefit_cost_year

    # Determine if a discount applies to the benefits cost
    def discount_applies(self, name):
        if name.lower()[0] == self.discount_letter:
            return True
        else:
            return False

    # Update the discount letter
    def update_discount_letter(self, discount_letter):
        self.discount_letter = discount_letter
        return

    # Update employee benefits cost
    def update_employee_benefit_cost_year(self, employee_benefit_cost_year):
        self.employee_benefit_cost_year = employee_benefit_cost_year
        return

    # Update dependent benefits cost
    def update_dependent_benefit_cost_year(self, dependent_benefit_cost_year):
        self.dependent_benefit_cost_year = dependent_benefit_cost_year
        return

    # Returns discount amount applied by matching discount letter
    def get_discount_amount(self):
        return self.discount_amount


# Calculate benefits discount; if applicable
def calculate_discounts(name, benefits):
    total_benefit_cost_percentage = 0.0
    if benefits.discount_applies(name):
        total_benefit_cost_percentage += (1.0 - benefits.discount_amount)
    else:
        total_benefit_cost_percentage += 1.0
    return total_benefit_cost_percentage


# Calculate benefits cost per year for the employee and dependents
def calculate_benefit_cost_year(employee, benefits):
    total_benefit_cost_year = 0
    total_benefit_cost_year += benefits.employee_benefit_cost_year * calculate_discounts(employee.employee_name, benefits)
    for name in employee.dependents:
        total_benefit_cost_year += (benefits.dependent_benefit_cost_year * (calculate_discounts(name, benefits)))

    return total_benefit_cost_year


# Returns the employee pay information (Gross Pay, Deduction/Benefits Cost, and Net Pay)
def report_benefit_costs(employee, benefits):
    report = []

    employee_pay_year = employee.paychecks_year * employee.pay_paycheck
    employee_benefit_cost_year = calculate_benefit_cost_year(employee, benefits)
    employee_net_year = employee_pay_year - employee_benefit_cost_year

    report.append(employee_pay_year)
    report.append(employee_benefit_cost_year)
    report.append(employee_net_year)
    return report


# Converts the Yearly report to Monthly
def report_conv_month(report_in):
    report_out = []
    for item in report_in:
        report_out.append(round(item/12, 2))
    return report_out


# Converts the yearly report to per paycheck
def report_conv_paycheck(report_in, employee):
    report_out = []
    for item in report_in:
        report_out.append(round(item/employee.paychecks_year, 2))
    return report_out
