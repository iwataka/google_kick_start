import math

T = int(input())
for t in range(T):
    Z = int(input())

    Z_sqrt = math.ceil(math.sqrt(Z))
    larger_prime = Z_sqrt
    while True:
        if all(larger_prime % i != 0 for i in range(2, min(larger_prime, math.ceil(math.sqrt(larger_prime)) + 1))):
            break
        larger_prime += 1
    smaller_prime = Z_sqrt - 1
    while True:
        if all(smaller_prime % i != 0 for i in range(2, min(smaller_prime, math.ceil(math.sqrt(smaller_prime)) + 1))):
            break
        smaller_prime -= 1
    prime_product = larger_prime * smaller_prime
    if prime_product <= Z:
        result = prime_product
    else:
        much_smaller_prime = smaller_prime - 1
        while True:
            if all(much_smaller_prime % i != 0 for i in range(2, min(much_smaller_prime, math.ceil(math.sqrt(much_smaller_prime)) + 1))):
                break
            much_smaller_prime -= 1
        result = smaller_prime * much_smaller_prime
    print(f"Case #{t + 1}: {result}")
