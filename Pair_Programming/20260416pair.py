arr = []
check = [[[0 for _ in range(10)] for _ in range(9)] for _ in range(3)] #x, y, block
slv=0

def solve_sdk(x, y):
    global slv
    if(y == 9):
        y = 0
        x += 1
        if(x == 9):
            slv=1
            return
    
    if(arr[x][y] != 0): return solve_sdk(x, y + 1)
    
    for i in range(1, 10):
        if(check[0][x][i] or check[1][y][i] or check[2][((x // 3) * 3 + y // 3)][i]): continue
        check[0][x][i] = 1
        check[1][y][i] = 1
        check[2][((x // 3) * 3 + y // 3)][i] = 1
        arr[x][y] = i
        solve_sdk(x, y + 1)
        if slv : break
        arr[x][y]=0
        check[0][x][i] = 0
        check[1][y][i] = 0
        check[2][((x // 3) * 3 + y // 3)][i] = 0

for i in range(9):
    arr.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if(arr[i][j] == 0): continue
        check[0][i][arr[i][j]] = 1
        check[1][j][arr[i][j]] = 1
        check[2][((i // 3) * 3 + j // 3)][arr[i][j]] = 1

solve_sdk(0,0)

for i in range(9):
    for j in range(9):
        print(arr[i][j],end=" ")
    print()