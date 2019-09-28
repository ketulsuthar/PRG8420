#Writea modulethat prompts the user for an integer and then returns the factorial of that integer


def main(a_number):
    """This function calculate factorial of given number.
    a_number : int
    """
    factorial = 1
    for i in range(1,a_number+1):
        factorial = factorial * i # IDEA: Multiply number from 1 to Given number
    print("Factorial of ",a_number, 'is', factorial)


if __name__ == '__main__':
    try:
        no = int(input("Enter number :"))
        main(no)
    except:
        print("Enter numeric value.")
