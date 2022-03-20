T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    S = input()
    goodness_score = 0
    for i in range(N//2):
        if S[i] != S[N - 1 - i]:
            goodness_score += 1
    print(f"Case #{t + 1}: {abs(K - goodness_score)}")
