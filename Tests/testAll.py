from Tests.testDomeniu import testCheltuiala
from Tests.funct_tests import test_delete_all_costs_for_apartement, test_add_sum_to_date, \
    test_the_biggest_expense_for_every_type, test_ordering_expenses_descending_by_amount
from Tests.crud_tests import test_create, test_read, test_update, test_delete
from Tests.undo_redo_tests import test_undo_redo


def runAllTests():
    testCheltuiala()
    test_create()
    test_read()
    test_update()
    test_delete()
    test_delete_all_costs_for_apartement()
    test_add_sum_to_date()
    test_the_biggest_expense_for_every_type()
    test_ordering_expenses_descending_by_amount()
    
