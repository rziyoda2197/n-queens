def n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def solve_n_queens(n, row, board):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve_n_queens(n, row + 1, board)

    result = []
    solve_n_queens(n, 0, [-1]*n)
    return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

n = 4
print(n_queens(n))
```

Kodda quyidagilar mavjud:

- `is_safe` funksiyasi quyidagi shartlarni tekshiradi:
  - Qirolicha hozirgi satrda bo'lganligi.
  - Qirolicha hozirgi satrda bo'lganligi.
  - Qirolicha hozirgi satrda bo'lganligi.
- `solve_n_queens` funksiyasi quyidagilarni amalga oshiradi:
  - Qirolicha hozirgi satrda bo'lganligini tekshiradi.
  - Qirolicha hozirgi satrda bo'lganligini tekshiradi.
  - Qirolicha hozirgi satrda bo'lganligini tekshiradi.
- `n_queens` funksiyasi quyidagilarni amalga oshiradi:
  - Qirolicha hozirgi satrda bo'lganligini tekshiradi.
  - Qirolicha hozirgi satrda bo'lganligini tekshiradi.
  - Qirolicha hozirgi satrda bo'lganligini tekshiradi.
