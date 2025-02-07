def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]

print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))