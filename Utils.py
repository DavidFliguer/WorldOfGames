import sys, os
import platform

SCORES_FILE_NAME = "Score.txt"
BAD_RETURN_CODE = -1

def screen_cleaner():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')


def ask_for_numeric_input(message, minimum_value=(-sys.maxsize - 1), maximum_value=sys.maxsize, convert_to_int=True
                          ):
    """
    Helper function that allows to ask for an input until the input is

    A) Numeric
    B) In the desired range (If no range is specified then a big range is the default)

    :param message: The input message to the user both the first time and the next times (If needed)
    :param minimum_value: Minimum value of the range (Including)
    :param maximum_value: Maximum value of the range (Including)
    :return: The user input which after the validations should be already OK
    """
    # By default assume that the user input is not good
    user_input_is_ok = False

    # Calculate once the range (Should be more efficient that calculating it again each time that we ask for input
    range_to_validate = range(minimum_value, maximum_value + 1)

    # Iterate until the user input is OK, since the default is false, we will ask for input at least the first time
    while not user_input_is_ok:
        user_input = input(message + "\n")
        if user_input.isdigit():
            if int(user_input) in range_to_validate:
                # If is both numeric and in the range then we can exit the loop
                user_input_is_ok = True
            else:
                print("Input is not in the range, should be a number between {} and {} \n".format(minimum_value,
                                                                                                  maximum_value))
        else:
            print("Input should be a number \n")
    # Here we already exited the loop so input should be an OK input
    if convert_to_int:
        return int(user_input)
    else:
        return user_input
