
##
## Small function to compute Fibonacci numbers
##
def compute_Fibonacci(n_numbers):
    return_list = [0, 1]
    for i in range(2,n_numbers,1):
        Fib = return_list[i-1]  + return_list[i-2]
        return_list.append(Fib)
    return return_list
