T = int(input())
for t in range(T):
    R, C = map(int, input().split())
    grid = []
    for r in range(R):
        grid.append(list(map(int, input().split())))

    n_boxes_to_add = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            upper_height = grid[r - 1][c] + n_boxes_to_add[r - 1][c] if r > 0 else 0
            left_height = grid[r][c - 1] + n_boxes_to_add[r][c - 1] if c > 0 else 0
            neighbor_height = max(upper_height, left_height)
            if grid[r][c] < neighbor_height:
                n_boxes_to_add[r][c] = neighbor_height - grid[r][c] - 1

    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            lower_height = grid[r + 1][c] + n_boxes_to_add[r + 1][c] if r < R - 1 else 0
            right_height = grid[r][c + 1] + n_boxes_to_add[r][c + 1] if c < C - 1 else 0
            neighbor_height = max(lower_height, right_height)
            if grid[r][c] < neighbor_height:
                _n_boxes_to_add = neighbor_height - grid[r][c] - 1
                n_boxes_to_add[r][c] = max(n_boxes_to_add[r][c], _n_boxes_to_add)

    print(f"Case #{t + 1}: {sum(sum(n_boxes_to_add, []))}")
