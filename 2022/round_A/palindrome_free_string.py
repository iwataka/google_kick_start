def generate_question_patterns(length, *prefixes):
    if length == 1:
        yield from prefixes
        yield 1
        yield from prefixes
        yield 0
    else:
        yield from generate_question_patterns(length - 1, *prefixes, 1)
        yield from generate_question_patterns(length - 1, *prefixes, 0)


def has_palindrome(digits):
    for i in range(len(digits) - 4):
        if digits[i] == digits[i + 4] and digits[i+1] == digits[i + 3]:
            return True
        if len(digits) - 5 > i and digits[i] == digits[i + 5] and digits[i+1] == digits[i + 4] and digits[i+2] == digits[i + 3]:
            return True
    return False


def check_no_palindrome_is_possible(S, n_questions):
    qps = generate_question_patterns(n_questions)
    try:
        while True:
            pattern = []
            for d in S:
                if d == '?':
                    pattern.append(next(qps))
                else:
                    pattern.append(int(d))
            if not has_palindrome(pattern):
                return pattern
    except StopIteration:
        return False


T = int(input())
for i in range(T):
    N = int(input())
    S = input()

    if N < 5:
        print(f"Case #{i+1}: POSSIBLE")
        continue

    n_questions = S.count('?')
    if n_questions >= N - 4:
        print(f"Case #{i+1}: POSSIBLE")
        continue

    result = True
    for w in range(5, N + 1):
        sub_S = S[:w]
        sub_n_questions = sub_S.count('?')
        if not check_no_palindrome_is_possible(sub_S, sub_n_questions):
            result = False
            break
    if result:
        print(f"Case #{i+1}: POSSIBLE")
    else:
        print(f"Case #{i+1}: IMPOSSIBLE")
