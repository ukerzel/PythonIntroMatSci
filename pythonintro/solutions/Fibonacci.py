





##
## define relevant functions
##
def compute_Fibonacci(n_numbers):
    return_list = [0, 1]
    for i in range(2,n_numbers,1):
        Fib = return_list[i-1]  + return_list[i-2]
        return_list.append(Fib)
    return return_list


##
## Main program
## Python uses the name to indicate the main program. If the program is executed, the code below is called.
##

if __name__ == '__main__':

    # get 10 Fibonacci numbers
    Fib = compute_Fibonacci(n_numbers=10)

    # write the Fibonacci numbers to a file
    with open('fibonacci.txt','w') as f:
        for number in Fib:
            f.write(str(number) + '\n')

    
    

