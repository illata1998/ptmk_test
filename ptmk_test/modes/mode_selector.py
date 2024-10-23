from ptmk_test.modes.mode_1 import create_employees_table
from ptmk_test.modes.mode_2 import create_and_save_employee
from ptmk_test.modes.mode_3 import find_and_show_unique_employees
from ptmk_test.modes.mode_4 import fill_employees_table
from ptmk_test.modes.mode_5 import select_f_male_employees

MODES = {
    '1': create_employees_table,
    '2': create_and_save_employee,
    '3': find_and_show_unique_employees,
    '4': fill_employees_table,
    '5': select_f_male_employees
}

def get_mode_function(mode: str) -> callable:
    """
    Retrieves the function corresponding to the given mode.

    Args:
        mode (str): The mode number as a string.

    Returns:
        function: The function associated with the given mode,
                  or None if the mode is not found.
    """
    return MODES.get(mode)
