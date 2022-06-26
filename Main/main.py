from art import logo

print(logo)


def add(n1 , n2):
    return n1 + n2


def subtract(n1 , n2):
    return n1 - n2


def multiply(n1 , n2):
    return n1 * n2


def divide(n1 , n2):
    return n1 / n2


dic = {
    '+': add ,
    '-': subtract ,
    '*': multiply ,
    '/': divide
}


def calculator():
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    for i in dic:
        print(i)
    operation_input = input("Select one of the above operation: ")

    calculation_function = dic[operation_input]
    first_answer = calculation_function(n1 , n2)

    print(f"{n1} {operation_input} {n2} = {first_answer}")

    condition = True
    while condition:
        choice = input(f"Do you want to use another operation in {first_answer} ? (y/n): ")
        if choice == 'y' or choice == 'Y':
            n3 = float(input("Enter the another number: "))
            operation_input = input("Select one of the above operation: ")

            calculation_function = dic[operation_input]
            second_answer = calculation_function(first_answer , n3)
            print(f"{first_answer} {operation_input} {n3} = {second_answer}")
            first_answer = second_answer
            continue
        else:
            sec_choice = input("Do you want to use this program again ? (y/n): ")
            if sec_choice == 'y' or sec_choice == 'Y':
                calculator()
            else:
                print("Thank You")
                break


calculator()
