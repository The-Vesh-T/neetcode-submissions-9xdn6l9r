class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row, check col, check squar
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[col][i] == '.':
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        start_pos =[(0,0), (0,3), (0,6),
                    (3,0), (3,3), (3,6),
                    (6,0), (6,3), (6,6)]
        #with these start positions jus tierate through in a tighter loop
        for r, c in start_pos:
            seen = set()
            for row in range(r, r+3):
                for col in range(c, c+3):
                    if board[row][col] == '.':
                        continue
                    if item in seen:
                        return False
                    seen.add(board[row][col])
        return True




