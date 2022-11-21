def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)




def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)




def compareTo(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0
    elif len(s1) == 0:
        return -1
    elif len(s2) == 0:
        return 1

    if s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])


if __name__ == '__main__':
    print(f"fibonacci(8) = {fibonacci(8)}")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"gcd(24, 56) = {gcd(24, 56)}")
    print(f"gcd(100, 45) = {gcd(100, 45)}")
    print(f"compareTo('Alain', 'Alan') = {compareTo('Alain', 'Alan')}")
    print(f"compareTo('Rocker', 'Rocker') = {compareTo('Rocker', 'Rocker')}")
