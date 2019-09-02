'''
Solution to Project Euler Problem 2:
https://projecteuler.net/problem=2
'''
def evenFibonacci(max):
    '''
    Returns sum of even terms in Fibonacci sequence below {max}
    '''
    a, b = 0, 1
    sum = 0
    while b < max:
        #print('b:', b)
        if b % 2 == 0:
            sum += b
        a, b = b, a+b

    return sum


def main():
    max = 4000000
    sum = evenFibonacci(max)
    print(f"Sum of even terms in Fibonacci sequence below {max}: {sum}")


if __name__ == "__main__":
    main()
