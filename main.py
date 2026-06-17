first_number = int(input('Enter a value: '))
second_number = int(input('Enter another value: '))

option = int(input(
    'Your values are {} and {}\n'
    '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
    '>>>>> What would you like to do?\n'
    ' [1] Add\n'
    ' [2] Multiply\n'
    ' [3] Greater Number\n'
    ' [4] New Numbers\n'
    ' [5] Exit Program\n'.format(first_number, second_number)
))

while option != 5:
    if option == 1:
        option = int(input(
            'The sum of {} and {} is {}\n'
            '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
            '>>>>> What would you like to do now?\n'
            ' [1] Add\n'
            ' [2] Multiply\n'
            ' [3] Greater Number\n'
            ' [4] New Numbers\n'
            ' [5] Exit Program\n'.format(
                first_number,
                second_number,
                first_number + second_number
            )
        ))

    elif option == 2:
        option = int(input(
            'The product of {} and {} is {}\n'
            '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
            '>>>>> What would you like to do now?\n'
            ' [1] Add\n'
            ' [2] Multiply\n'
            ' [3] Greater Number\n'
            ' [4] New Numbers\n'
            ' [5] Exit Program\n'.format(
                first_number,
                second_number,
                first_number * second_number
            )
        ))

    elif option == 3:
        if first_number > second_number:
            message = '{} is greater than {}'.format(first_number, second_number)
        elif second_number > first_number:
            message = '{} is greater than {}'.format(second_number, first_number)
        else:
            message = 'Both numbers are equal'

        option = int(input(
            '{}\n'
            '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
            '>>>>> What would you like to do now?\n'
            ' [1] Add\n'
            ' [2] Multiply\n'
            ' [3] Greater Number\n'
            ' [4] New Numbers\n'
            ' [5] Exit Program\n'.format(message)
        ))

    elif option == 4:
        first_number = int(input('Enter a value: '))
        second_number = int(input('Enter another value: '))

        option = int(input(
            'Your values are {} and {}\n'
            '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
            '>>>>> What would you like to do?\n'
            ' [1] Add\n'
            ' [2] Multiply\n'
            ' [3] Greater Number\n'
            ' [4] New Numbers\n'
            ' [5] Exit Program\n'.format(first_number, second_number)
        ))

print('END OF PROGRAM')
