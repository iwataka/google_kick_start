T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    result = 0
    for n in range(A, B+1):
        sum = 0
        product = 1
        for d in str(n):
            sum += int(d)
            product *= int(d)
        if product % sum == 0:
            result += 1
    print(f"Case #{i+1}: {result}")
