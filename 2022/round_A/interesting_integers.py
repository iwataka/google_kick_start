def count_interesting_integers(N):
    if N == 0:
        return 0

    count = 0
    for L in range(1, len(str(N))):
        count += count_interesting_integers_with_number_of_digits(L)
    count += count_interesting_integers_with_prefix_of_N(N, P=1, S=0, digit_index=0, is_first_digit=True)
    return count


def count_interesting_integers_with_number_of_digits(L):
    count = 0
    for digit in range(1, 10):
        count += f1(L - 1, P=digit, S=digit)
    return count


def count_interesting_integers_with_prefix_of_N(N, P, S, digit_index, is_first_digit):
    if digit_index == len(str(N)):
        return 1 if S > 0 and P % S == 0 else 0
    if is_first_digit:
        digit_start = 1
    else:
        digit_start = 0

    count = 0
    for digit in range(digit_start, int(str(N)[digit_index])):
        count += f1(len(str(N)) - digit_index - 1, P * digit, S + digit)

    count += count_interesting_integers_with_prefix_of_N(
        N,
        P * int(str(N)[digit_index]),
        S + int(str(N)[digit_index]),
        digit_index + 1,
        is_first_digit=False,
    )

    return count


f1_result = {}


def f1(L, P, S):
    if (L, P, S) in f1_result:
        return f1_result[(L, P, S)]

    if L == 0:
        return 1 if P % S == 0 else 0

    count = 0
    for digit in range(0, 10):
        count += f1(L - 1, P * digit, S + digit)

    f1_result[(L, P, S)] = count
    return count


T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    b_result = count_interesting_integers(B)
    a_result = count_interesting_integers(A - 1)
    result = b_result - a_result
    print(f"Case #{t + 1}: {result}")
