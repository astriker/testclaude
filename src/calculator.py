def add(a, b):
    """두 수를 더한다."""
    return a + b


def subtract(a, b):
    """두 수를 뺀다."""
    return a - b


def multiply(a, b):
    """두 수를 곱한다."""
    return a * b


def divide(a, b):
    """두 수를 나눈다. 0으로 나누면 ValueError 발생."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """a의 b제곱을 반환한다."""
    return a**b


def factorial(n):
    """n의 팩토리얼을 반환한다. 음수는 ValueError 발생."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a, b):
    """두 수의 최대공약수를 반환한다."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """두 수의 최소공배수를 반환한다."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def is_prime(n):
    """n이 소수인지 판별한다."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
