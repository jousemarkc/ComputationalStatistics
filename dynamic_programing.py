def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)

def fibonacci_dynamic(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dynamic(n - 1, memo) + fibonacci_dynamic(n - 2, memo)
        memo[n] = resultado
        return resultado


if __name__ == '__main__':
    n = int(input('Choose a number: '))
    # result = fibonacci_recursive(n)
    result = fibonacci_dynamic(n)
    print(result)