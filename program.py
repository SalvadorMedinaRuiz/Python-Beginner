import math
#Salvador Medina-Ruiz COSC 341

#Problem 1: a function that computes the value of mathematical constant π. The value of π 
#can be computed using the infinite series p = 4(1 – 1/3 + 1/5 – 1/7 + 1/9 – 1/11 + . . .)
def compute_pi(n):
    pi = 0
    next_num_in_pi = 0
    sum = 0
    
    for i in range(0, n, 1):
        next_num_in_pi = math.pow(-1, i)/(2*i+1)
        sum += next_num_in_pi
    
    pi = 4 * sum
    return pi

#Problem 2: a function that computes the square root of a given number.
def compute_sqrt(x):
    sqrt = 1
    last_guess = 1
    next_guess = 0
    
    for i in range(0, 10, 1):
        next_guess = 0.5*(last_guess + x/last_guess)
        last_guess = next_guess
    sqrt = next_guess
    return sqrt

#Problem 3: a  function  that  decides  whether  a  given  number  is  a  prime  or  not.  A  prime 
#number is a number that is divisible only by 1 and itself.
def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, (n//2)+1, 1):
        if n % i == 0:
            return False
    return True

#displays  all  prime numbers less than or equal to n.
def display_primes(n):
    for i in range(0, n+1, 1):
        boolean_result = is_prime(i)
        if boolean_result == True:
            print(i)

#Problem 4: eads student names and their scores 
#from  a  user  and  displays  the  following:  the  average  score,  the  minimum  score,  the 
#maximum score, and the students who received the minimum and maximum scores.
def process_scores():
    name = 'test'
    max_score_name = 'test'
    min_score_name = 'test'
    
    score = 0
    all_the_scores = 0
    average_score = 0
    number_of_scores = 0
    max_score = 0
    min_score = 100
    #Actual loops that asks for scores and names
    while name.upper() != 'Q':
        name = input('Please enter the first name only of the student followed by their score, seperated by a space. Enter q to quit: ')
        if name.upper() != 'Q':
            name, score = name.split()
            score = int(score)
            all_the_scores += score
            number_of_scores = number_of_scores + 1
            
            if score > max_score:
                max_score_name = name
                max_score = score
            
            if min_score > score:
                min_score_name = name
                min_score = score
    average_score = all_the_scores/number_of_scores
    print('The maximum score was a', max_score,'which was achieved by', max_score_name)
    print('The lowest score was a', min_score,'which was achieved by', min_score_name)
    print('The average score was', average_score)

#Problem 5:  function that determines the tax amount according to the following tax rules.  
#The tax rate depends on the income, the marital status, and the state residency.
def compute_tax(income, status, state):
    tax_amount = 0
    tax_rate = 0
    if state.upper() == 'I':
        if status[0].upper() == 'S' and income < 30000:
            tax_rate = .2
        elif status[0].upper() == 'S' and income >= 30000:
            tax_rate = .25
        elif status[0].upper() == 'M' and income < 50000:
            tax_rate = .1
        elif status[0].upper() == 'M' and income >= 50000:
            tax_rate = .15
    elif state.upper() == 'O':
        if status[0].upper() == 'S' and income < 30000:
            tax_rate = .17
        elif status[0].upper() == 'S' and income >= 30000:
            tax_rate = .22
        elif status[0].upper() == 'M' and income < 50000:
            tax_rate = .07
        elif status[0].upper() == 'M' and income >= 50000:
            tax_rate = .12
    tax_amount = income * tax_rate
    return tax_amount

#Problem 6: a  function  that  solves  a  given  quadratic  equation.
def solve_quadtratic(a, b, c):
    solution1 = 0
    solution2 = 0
    does_it_have_solution = b * b - 4*a*c
    
    if does_it_have_solution >= 0:
        solution1 = (-b + math.sqrt(does_it_have_solution))/(2*a)
        solution2 = (-b - math.sqrt(does_it_have_solution))/(2*a)
    
    return solution1, solution2

#Problem 7: sorts a given list of numbers. 
def sort(list):
    list_copy = [0]*len(list)
    #Actually copies the list
    for i in range(0, len(list), 1):
        list_copy[i] = list[i]
    
    list_length = len(list_copy)
    #Sorts the list using selection sort
    for i in range(list_length - 1):
        min_value = i
        for i2 in range(i + 1, list_length, 1):
            if list_copy[i2] < list_copy[min_value]:
                min_value = i2
        
        if min_value != i:
            temp_list_value = list_copy[i]
            list_copy[i] = list_copy[min_value]
            list_copy[min_value] = temp_list_value
    return list_copy

#Problem 8: a function that automatically generates the user id and the password for the user. 
#The user id and the pass words are based on the user’s last name and first name. 
def id_password(first, last):
    first_name = first.upper()
    last_name = last.upper()
    
    user_id = first_name[0] + last_name
    user_password = first_name[0] + first_name[-1] + last_name[0] + last_name[1] + last_name[2] + str(len(first_name)) + str(len(last_name))
    
    return user_id, user_password

#Problem 9: a function that reads an input file and creates a sorted output file. 
def file_sort(infile, outfile):
    file_input = open(infile, 'r')
    file_output = open(outfile, 'w')
    
    line = file_input.readline()
    number_of_students = int(line)
    
    student_id = [0]*number_of_students
    student_name = [0]*number_of_students
    student_gpa = [0]*number_of_students
    
    #Reading each line in input file, one by one
    for i in range(0, number_of_students, 1):
        line = file_input.readline()
        student_id[i], student_name[i], student_gpa[i] = line.split()
        student_id[i] = int(student_id[i])
        student_gpa[i] = float(student_gpa[i])
    
    #Writing to the output file
    file_output.write(str(number_of_students) + '\n')
    for i in range(0, number_of_students, 1):
        i2 = i + 1
        for i2 in range(i2, number_of_students, 1):
            if student_id[i] > student_id[i2]:
                temp_id = student_id[i]
                student_id[i] = student_id[i2]
                student_id[i2] = temp_id
                
                temp_name = student_name[i]
                student_name[i] = student_name[i2]
                student_name[i2] = temp_name
                
                temp_gpa = student_gpa[i]
                student_gpa[i] = student_gpa[i2]
                student_gpa[i2] = temp_gpa
    
    for i in range(0, number_of_students, 1):
        file_output.write(str(student_id[i]) + ' ' + str(student_name[i]) + ' ' + str(student_gpa[i]) + '\n')
    
    file_input.close()
    file_output.close()

#main program
print('Welcome to the Program!')
user_input = input('Enter a number to pick an option: 1-Computing Pi, 2-Computing Square root, 3-Display Primes, 4-Processing Grades, 5-Computing Tax, 6-Solving Quadratic, 7-Sort List, 8-ID and Password, 9-File Sort, 10-Quit the Program: ')
user_input = int(user_input)
while user_input != 10:
    #Problem 1
    if user_input == 1:
        pi_input = input('Please enter an integer that you would like to compute PI for: ')
        pi_input = int(pi_input)
        pi_result = compute_pi(pi_input)
        print('PI is', pi_result)
    #Problem 2
    elif user_input == 2:
        sqrt_input = input('Please enter a number that you would like to compute the square root for: ')
        sqrt_input = float(sqrt_input)
        sqrt_result = compute_sqrt(sqrt_input)
        print('The result for the Square Root is:', sqrt_result)
    #Problem 3
    elif user_input == 3:
        prime_input = input('Please enter an integer that you would like to see if it\'s a prime number or not: ')
        prime_input = int(prime_input)
        prime_result = is_prime(prime_input)
        if prime_result == True:
            print(prime_input, 'is prime!')
        elif prime_result == False:
            print(prime_input, 'is not prime.')
        print('All the numbers from before', prime_input,'that are prime:')
        display_primes(prime_input)
    #Problem 4
    elif user_input == 4:
        process_scores()
    #Problem 5
    elif user_input == 5:
        income_amount = input('Enter your income as an int, maritial status (Married or Single), and if your in or out of state (i or o): ')
        income_amount, status_sm, i_o = income_amount.split()
        income_amount = int(income_amount)
        tax_result = compute_tax(income_amount, status_sm, i_o)
        print('The tax amount is:', tax_result)
    #Problem 6
    elif user_input == 6:
        numbera = input('Please enter 3 numbers that you would like to input into the quadratic equation: ')
        numbera, numberb, numberc = numbera.split()
        numbera = float(numbera)
        numberb = float(numberb)
        numberc = float(numberc)
        quad_result1, quad_result2 = solve_quadtratic(numbera, numberb, numberc)
        if quad_result1 != 0:
            print('The solutions are', quad_result1, quad_result2)
        else:
            print('There are no solutions')        
    #Problem 7
    elif user_input == 7:
        user_list = []
        list_input = input('Please enter a list of numbers and then hit enter when done: ')
        user_list = list_input.split()
        for i in range(0, len(user_list), 1):
            user_list[i] = int(user_list[i])
        print('The sorted list is:', sort(user_list))
    #Problem 8
    elif user_input == 8:
        user_name_first = input('Please enter your first and last name for an ID and password: ')
        user_name_first, user_name_last = user_name_first.split()
        user_name_id, user_name_password = id_password(user_name_first, user_name_last) 
        print('Your ID is', user_name_id, 'and your password is', user_name_password)
    #Problem 9
    elif user_input == 9:
        input_name = input('Please enter the name of the input file you wish to be sorted, and the output file that is to be created: ')
        input_name, output_name = input_name.split()
        file_sort(input_name, output_name)
        print('Done! Please checkout output file')
    user_input = input('Enter a number to pick an option: 1-Computing Pi, 2-Computing Square root, 3-Display Primes, 4-Processing Grades, 5-Computing Tax, 6-Solving Quadratic, 7-Sort List, 8-ID and Password, 9-File Sort, 10-Quit the Program: ')
    user_input = int(user_input)
print('You quit the program! Have a good day')