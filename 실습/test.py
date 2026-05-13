arr = []
def is_valid(row, col, num):
    for i in range(9):
        if arr[row][i] == num:
            return False
    for i in range(9):
        if arr[i][col] == num:
            return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if arr[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku():
    """재귀(Recursion)를 사용하여 빈 칸을 채웁니다."""
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(row, col, num):
                        if solve_sudoku(): 
                            return True 
                        arr[row][col] = 0 
                return False
    return True

for i in range(9):
    arr.append(list(map(int, input().split())))
solve_sudoku()
for i in range(9):
    for j in range(9):
        print(arr[i][j],end=" ")
    print()