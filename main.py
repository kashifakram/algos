from fib import fib
from greedy import min_coins
from divide_conq import bin_search_algo
from dyn_prog import nth_fibonacci

def main():
    print("main program starts")    
    fib(40)
    print("Min coin to get 30 is", min_coins([5,10,2], 30))

    sear_arr = [2, 4, 7, 12, 15, 21, 23]
    print("12 is at index", bin_search_algo(sear_arr, 90))

    n = 10
    result = nth_fibonacci(n)
    print("The", n, "th Fibonacci number is:", result)



    print("thank you...")

if __name__ == "__main__":
    main()