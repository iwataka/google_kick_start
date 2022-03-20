T = int(input())
for t in range(T):
    R, C = map(int, input().split())
    grid = []
    for r in range(R):
        grid.append(list(map(int, input().split())))

    top = [[0] * C for _ in range(R)]
    left = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                continue
            top[r][c] = top[r - 1][c] + 1 if r > 0 else grid[r][c]
            left[r][c] = left[r][c - 1] + 1 if c > 0 else grid[r][c]

    bottom = [[0] * C for _ in range(R)]
    right = [[0] * C for _ in range(R)]
    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            if grid[r][c] == 0:
                continue
            bottom[r][c] = bottom[r + 1][c] + 1 if r < R - 1 else grid[r][c]
            right[r][c] = right[r][c + 1] + 1 if c < C - 1 else grid[r][c]

    result = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                continue
            result += max(min(top[r][c] // 2, left[r][c]) + min(top[r][c], left[r][c] // 2) - 2, 0)
            result += max(min(top[r][c] // 2, right[r][c]) + min(top[r][c], right[r][c] // 2) - 2, 0)
            result += max(min(bottom[r][c] // 2, left[r][c]) + min(bottom[r][c], left[r][c] // 2) - 2, 0)
            result += max(min(bottom[r][c] // 2, right[r][c]) + min(bottom[r][c], right[r][c] // 2) - 2, 0)

    print(f"Case #{t + 1}: {result}")
