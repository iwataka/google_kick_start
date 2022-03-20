T = int(input())
for i in range(T):
    I = input()
    P = input()
    i_P = 0
    result = 0
    for c in I:

        while True:
            # break if not found
            if len(P) <= i_P:
                result = -1
                break

            # if found, go to next
            if c == P[i_P]:
                i_P += 1
                break
            else:
                i_P += 1
                result += 1

        if result < 0:
            break

    result += (len(P) - i_P)

    if result < 0:
        print(f"Case #{i+1}: IMPOSSIBLE")
    else:
        print(f"Case #{i+1}: {result}")
