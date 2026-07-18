class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [0] * 9
            col = [0] * 9
            for j in range(9):
                if board[i][j].isdigit():
                    num = int(board[i][j])
                    if row[num-1] == 1:
                        return False
                    row[num-1] = 1
                if board[j][i].isdigit():
                    num = int(board[j][i])
                    if col[num-1] == 1:
                        return False
                    col[num-1] = 1
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                dups = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] == ".":
                            continue
                        if board[k][l] in dups:
                            return False
                        dups.add(board[k][l])
        return True