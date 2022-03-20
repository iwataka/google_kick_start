def has_no_palindrome(head, tail):
    if len(tail) == 0:
        return head[0] != head[4] or head[1] != head[3]

    # if it has 5-length palindrome
    if head[0] == head[4] and head[1] == head[3]:
        return False

    next_char = tail[0]
    tail = tail[1:]
    # check if it doesn't have 6-length palindrome and go next
    if next_char == '?':
        return (
            (head[0] != '0' or head[1] != head[4] or head[2] != head[3]) and has_no_palindrome(head[1:] + ['0'], tail) or
            (head[0] != '1' or head[1] != head[4] or head[2] != head[3]) and has_no_palindrome(head[1:] + ['1'], tail)
        )
    else:
        return (head[0] != next_char or head[1] != head[4] or head[2] != head[3]) and has_no_palindrome(head[1:] + [next_char], tail)


def generate_patterns(head, tail):
    if len(tail) == 0:
        yield head
    else:
        next_char = tail[0]
        tail = tail[1:]
        if next_char == '?':
            yield from generate_patterns(head + ['0'], tail)
            yield from generate_patterns(head + ['1'], tail)
        else:
            yield from generate_patterns(head + [next_char], tail)


T = int(input())
for t in range(T):
    N = int(input())
    S = input()

    if N < 5:
        print(f"Case #{t+1}: POSSIBLE")
        continue

    head = [c for c in S[:5]]
    tail = [c for c in S[5:]]
    result = False
    for pattern in generate_patterns([], head):
        if has_no_palindrome(pattern, tail):
            result = True
            break
    if result:
        print(f"Case #{t+1}: POSSIBLE")
    else:
        print(f"Case #{t+1}: IMPOSSIBLE")
