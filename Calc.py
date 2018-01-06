print(
        '''Hello!! everyone
        This application helps you in making some basic calculations
        According to the need , you can choose to the operations 
        you want to carry out
        '''
     )

count = 1

def add(one, two):
    return one+two

def sub(one, two):
    return one-two

def mul(one, two):
    return one*two

def div(one, two):
    return one/two

while(count==1):
    print(
            '''Choose the suitable opertaion you want to carry out
                1.Addtion
                2.Subtraction
                3.Multiplication
                4.Division
                5.Exit
            '''
         )
    task = eval(input('Enter the operation number \n:-'))
    if task == 1:
        num1, num2 = eval(input('Enter the two numbers seperated by comma \n:-'))
        sum = add(num1, num2)
        print('The sum of the two numbers is', sum)
    elif task == 2:
        num1, num2 = eval(input('Enter the two numbers seperated by comma \n:-'))
        diff = sub(num1, num2)
        print('The difference of the two numbers is', diff)

    elif task == 3:
        num1, num2 = eval(input('Enter the two numbers seperated by comma \n:-'))
        into = mul(num1, num2)
        print('The product of the two numbers is', into)

    elif task == 4:
        num1, num2 = eval(input('Enter the two numbers seperated by comma \n:-'))
        upon = div(num1, num2)
        print('The division of the two numbers is', upon)

    elif task == 5:
        count+=1
        exit()

    else:
        print('Sorry...you have entered an invalid choice')

    loop = input('\nDo you want to perform any another operation, [y/n] \n:-')
    if loop == 'y' or loop == 'Y':
        pass
    else:
        print('It was a pleasure helping you out\nSee you next time'
              '')
        count+=1
