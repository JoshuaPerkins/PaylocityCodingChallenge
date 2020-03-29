import pcc_main


def test_employee_create(input_name, employee):
    if input_name == employee.employee_name:
        result = 'Pass'
    else:
        result = 'Fail'
    print('Test Employee Create - Result: {}\n'
          '\tInput Name: {}\n'
          '\tEmployee Name: {}\n'
          .format(result, input_name, employee.employee_name))
    return result


def test_dependents_list(input_dependents, employee):
    if input_dependents == employee.dependents:
        result = 'Pass'
    elif input_dependents is None and employee.dependents == []:
        result = 'Pass'
    else:
        result = 'Fail'
    print('Test Dependents List - Result: {}\n'
          '\tInput Dependents: {}\n'
          '\tEmployee Dependents: {}\n'
          .format(result, input_dependents, employee.dependents))
    return result


def test_calculation(name, type, expected, actual):
    if expected == actual:
        result = 'Pass'
    else:
        result = 'Fail'
    print('{} Test Calculation {} - Result: {}\n'
          '\tInput Gross: {}, Deductions: {}, Net: {}\n'
          '\tEmployee Gross: {}, Deductions: {}, Net: {}\n'
          .format(name, type, result,expected[0], expected[1], expected[2],
                  actual[0], actual[1], actual[2]))
    return result


def test_results_stats(test_results):
    total_tests = len(test_results)
    fails = test_results.count('Fail')
    passes = test_results.count('Pass')
    fail_percent = 100*fails/total_tests
    pass_percent = 100*passes/total_tests

    print('Test Results Statistics:\n'
          '\tTotal Tests: {}\n'
          '\tPass Rate: {}% -- ({} Passes)\n'
          '\tFail Rate: {}% -- ({} Fails)\n'
          .format(total_tests, pass_percent, passes, fail_percent, fails))


if __name__ == '__main__':
    # Array of pass/fail results for test statistics
    test_results = []

    # Standard benefits use predetermined values
    general_benefits = pcc_main.Benefits()

    # Create employee variables for testing with expected results defined
    e1_name = 'Bob'
    e1_dependents = None
    e1_expected_pay_year = [52000.00, 1000.00, 51000.00]
    e1_expected_pay_month = [4333.33, 83.33, 4250.00]
    e1_expected_pay_check = [2000.00, 38.46, 1961.54]

    e2_name = 'Alice'
    e2_dependents = ['Joe']
    e2_expected_pay_year = [52000.00, 1400.00, 50600.00]
    e2_expected_pay_month = [4333.33, 116.67, 4216.67]
    e2_expected_pay_check = [2000.00, 53.85, 1946.15]

    e3_name = 'John'
    e3_dependents = ['April', 'Mary', 'Dan']
    e3_expected_pay_year = [52000.00, 2450.00, 49550.00]
    e3_expected_pay_month = [4333.33, 204.17, 4129.17]
    e3_expected_pay_check = [2000.00, 94.23, 1905.77]

    e4_name = None
    e4_dependents = None

    # Create Employee objects from employee variables
    my_e1 = pcc_main.Employee(e1_name, e1_dependents)
    my_e2 = pcc_main.Employee(e2_name, e2_dependents)
    my_e3 = pcc_main.Employee(e3_name, e3_dependents)
    my_e4 = pcc_main.Employee(e4_name, e4_dependents)

    # Create cost preview results for each employee with each type of output (yearly, monthly, per paycheck)
    e1_report_year = pcc_main.report_benefit_costs(my_e1, general_benefits)
    e2_report_year = pcc_main.report_benefit_costs(my_e2, general_benefits)
    e3_report_year = pcc_main.report_benefit_costs(my_e3, general_benefits)

    e1_report_month = pcc_main.report_conv_month(e1_report_year)
    e2_report_month = pcc_main.report_conv_month(e2_report_year)
    e3_report_month = pcc_main.report_conv_month(e3_report_year)

    e1_report_paycheck = pcc_main.report_conv_paycheck(e1_report_year, my_e1)
    e2_report_paycheck = pcc_main.report_conv_paycheck(e2_report_year, my_e2)
    e3_report_paycheck = pcc_main.report_conv_paycheck(e3_report_year, my_e3)

    # Test employee creation and name validation
    test_results.append(test_employee_create(e1_name, my_e1))
    test_results.append(test_employee_create(e2_name, my_e2))
    test_results.append(test_employee_create(e3_name, my_e3))
    test_results.append(test_employee_create(e4_name, my_e4))

    # Test employee dependents list validation
    test_results.append(test_dependents_list(e1_dependents, my_e1))
    test_results.append(test_dependents_list(e2_dependents, my_e2))
    test_results.append(test_dependents_list(e3_dependents, my_e3))
    test_results.append(test_dependents_list(e4_dependents, my_e4))

    # Test employee benefits cost calculations for all outputs (yearly, monthly, per paycheck)
    test_results.append(test_calculation(my_e1.employee_name, 'Yearly', e1_expected_pay_year, e1_report_year))
    test_results.append(test_calculation(my_e2.employee_name, 'Yearly', e2_expected_pay_year, e2_report_year))
    test_results.append(test_calculation(my_e3.employee_name, 'Yearly', e3_expected_pay_year, e3_report_year))

    test_results.append(test_calculation(my_e1.employee_name, 'Monthly', e1_expected_pay_month, e1_report_month))
    test_results.append(test_calculation(my_e2.employee_name, 'Monthly', e2_expected_pay_month, e2_report_month))
    test_results.append(test_calculation(my_e3.employee_name, 'Monthly', e3_expected_pay_month, e3_report_month))

    test_results.append(test_calculation(my_e1.employee_name, 'Per Paycheck', e1_expected_pay_check, e1_report_paycheck))
    test_results.append(test_calculation(my_e2.employee_name, 'Per Paycheck', e2_expected_pay_check, e2_report_paycheck))
    test_results.append(test_calculation(my_e3.employee_name, 'Per Paycheck', e3_expected_pay_check, e3_report_paycheck))

    # Report back test statistics for pass/fail ratio
    test_results_stats(test_results)

    # Keep console open until user has reviewed results and exit on user input
    input('Testing Complete: Please press "Enter" to exit.')
