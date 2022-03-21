T = int(input())
for t in range(T):
    N = int(input())
    S = input()

    result = []
    cur_length = 0
    prev_char = None
    for c in S:
        if prev_char is None or prev_char < c:
            cur_length += 1
        else:
            cur_length = 1
        prev_char = c
        result.append(cur_length)
    print(f"Case #{t+1}: {' '.join(map(str, result))}")
