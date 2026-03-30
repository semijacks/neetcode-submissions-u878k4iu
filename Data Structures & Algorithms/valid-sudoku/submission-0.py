class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grids = collections.defaultdict(set)

        for row in range(0, 9):
            for col in range(0,9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in grids[(row // 3, col // 3)]):
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                grids[(row // 3, col // 3)].add(board[row][col])

        return True
        