def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    """
    ########################################
    Code Your Program here
    ########################################
    """
    if num1 >= num2 and num1 >= num3:
        maxval = num1
    elif num2 >= num1 and num2 >= num3:
        maxval = num2
    else:
        maxval = num3

    if num1 <= num2 and num1 <= num3:
        minval = num1
    elif num2 <= num1 and num2 <= num3:
        minval = num2
    else:
        minval = num3

    if (minval == num2 and maxval == num3) or (maxval == num2 and minval == num3):
        median = num1
    elif (minval == num1 and maxval == num3) or (maxval == num1 and minval == num3):
        median = num2
    else:
        median = num3


    print(minval, median, maxval)
    ########################################
    # Do not delete the return statement
    ########################################
    return minval, median, maxval


if __name__ == '__main__':
    main()
