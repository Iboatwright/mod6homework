def main():
    twoValuesList = []
    requestList = [['integer', 'first whole number to compare'],
                   ['integer', 'second whole number to compare']]
    maxValue = ''

    fluffy_intro()

    twoValuesList = get_valid_inputs(requestList)

    maxValue = max_of_two([int(x) for x in twoValuesList])

    display_results(twoValuesList, maxValue)

    return None

# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('\nWelcome to the Max of Two Values program.\n'
          'This program determines which of two integers has the higher\n'
          'value. It then displays the results for your viewing pleasure.\n')
    return None


# get_valid_inputs requests input from the user then tests the input.
#   If invalid, it will alert the user and request the correct input.
# The parameter is a nested List of ordered pair Lists.
#   First value is the validation test and second is the user prompt.
def get_valid_inputs(requestsList):
    # local List to hold user inputs for return to calling module
    userInputs = []

    # Loop through each entry in requestList assigning each List pair
    #  to request.
    for request in requestsList:
        # untestedInput is a holding variable for testing user input validity.
        # First user prompt before testing loop
        untestedInput = prompt_user_for_input(request[1])

        # If test_value returns True, Not converts it to False and the While
        #  Loop will not execute.
        # If test_value returns False, the While executes and the user is
        #  prompted to enter a valid value.
        while (not test_value(request[0], untestedInput)):

            print('!!! Error: {} is not a valid value.'.format(untestedInput))
            untestedInput = (prompt_user_for_input(request[1]))

        # The user input tested valid and is appended to the userInputs List.
        userInputs.append(untestedInput)
    # for loop terminates and userInputs are returned to calling Module
    return userInputs


# prompt_user_for_item is passed a String to print to screen as part of a user
#   prompt.  Then returns it to the calling module.
def prompt_user_for_input(promptTerm):
    # promptTerm is a local variable to hold the value passed from the
    #   calling module.
    print('Please enter your {}.'.format(promptTerm))
    return input('  >> ')


# test_value uses the testCondition to select the proper test.
# It returns True or False to the calling Module.
def test_value(testCondition, testItem):
    # The If-Then-Else structure functions as a Switch for test selection.
    if testCondition == 'integer':
        # Try will try to convert testItem to an integer. If it succeeds
        #  True is returned to the calling module.  If int(testItem)
        #  creates an error, except will stop the error from writing to
        #  the screen and returns False.
        try:
           int(testItem)
           return True
        except:
            return False
    else:
        return None


# max_of_two compares the two validated user input integers and returns
#  the result.
def max_of_two(valuesList):
    if valuesList[0] == valuesList[1]:
        return 'equal'
    elif valuesList[0] > valuesList[1]:
        return '0'
    else:
        return '1'


# display_results is passed values used in print statements to display
#  the results of the program to the user.
def display_results(twoValuesList, maxValue):
    # This shows the value comparison and the results.  Output will vary
    # depending on the three possible outcomes.
    if maxValue == 'equal':
        print('\n{:^40}\n{:^40}'.format("You think you're so funny don't you?",
              "You entered the same number twice!"))
        print('{:-<40}\n{:^40}'.format('',
              '{0} == {0}'.format(twoValuesList[0])))
    elif maxValue == '0':
        print("\nYour first value is greater than your second value.")
        print('{:-<51}\n{:^51}'.format('',
              '{0} > {1}'.format(twoValuesList[0], twoValuesList[1])))
    else:
        print("\nYour second value is greater than your first value.")
        print('{:-<51}\n{:^51}'.format('',
              '{0} < {1}'.format(twoValuesList[0], twoValuesList[1])))
    return None


# Call the main function to run the program.
main()
