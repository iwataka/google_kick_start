T = int(input())
for i in range(T):
    N = input()
    sum = 0
    for j in N:
        sum += int(j)
    num_to_insert = 9 - (sum % 9)
    if num_to_insert == 9:
        result = N[:1] + "0" + N[1:]
    else:
        i_to_insert = next((i_to_insert for i_to_insert, num in enumerate(N) if int(num) > num_to_insert), -1)
        if i_to_insert < 0:
            result = N + str(num_to_insert)
        else:
            result = N[:i_to_insert] + str(num_to_insert) + N[i_to_insert:]
    print(f"Case #{i+1}: {result}")
