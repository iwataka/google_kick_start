T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    result = 0

    same_diff_subarray_stats = []  # [(length, diff, end_index)]
    prev_diff = 0
    prev_digit = 0
    prev_len = 0
    for i, d in enumerate(A):
        if i == 0:
            prev_len = 1
        elif i == 1:
            prev_diff = d - prev_digit
            prev_len = 2
        else:
            diff = d - prev_digit
            if diff == prev_diff:
                prev_len += 1
            else:
                same_diff_subarray_stats.append((prev_len, prev_diff, i - 1))
                prev_diff = diff
                prev_len = 2
        prev_digit = d

    same_diff_subarray_stats.append((prev_len, prev_diff, len(A) - 1))

    result = min(max(l + 1 for l, _, _ in same_diff_subarray_stats), len(A))

    for i in range(len(same_diff_subarray_stats) - 2):
        len1, diff1, end_index1 = same_diff_subarray_stats[i]
        len2, diff2, end_index2 = same_diff_subarray_stats[i + 1]
        len3, diff3, end_index3 = same_diff_subarray_stats[i + 2]
        if len2 == 2:
            if (A[end_index1 + 2] - A[end_index1]) == diff1 * 2:
                result = max(result, len1 + 2)
            if (A[end_index2] - A[end_index2 - 2]) == diff3 * 2:
                result = max(result, len3 + 2)

    for i in range(len(same_diff_subarray_stats) - 3):
        len1, diff1, end_index1 = same_diff_subarray_stats[i]
        len2, diff2, end_index2 = same_diff_subarray_stats[i + 1]
        len3, diff3, end_index3 = same_diff_subarray_stats[i + 2]
        len4, diff4, end_index4 = same_diff_subarray_stats[i + 3]
        if len2 == 2 and len3 == 2 and diff1 == diff4 and (A[end_index3] - A[end_index1]) == diff1 * 2:
            result = max(result, len1 + len4 + 1)

    print(f"Case #{t + 1}: {result}")
