class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidRows(board) and self.isValidCol(board) and         self.isValidSqr2(board)
    def isValidRows(self, board) -> bool:
        for i in board:
            lista = []
            for j in i:
                if j != '.':
                    lista.append(j)
            if len(set(lista)) != len(lista):
                return False
        return True
    def isValidCol(self, board) -> bool:
        for i in range(9):
            lista = []
            for j in range(9):            
                 if board[j][i] != '.':
                    lista.append(board[j][i])
            if len(set(lista)) != len(lista):
                return False
        return True
    def isValidSqr(self, board, x, y) -> bool:
        lista = []
        for i in range(x,x+3):
            for j in range(y, y+3):
                if board[i][j] != '.':
                    lista.append(board[i][j])
        print(lista)
        if len(set(lista)) != len(lista):
            return False
        return True
    def isValidSqr2(self, board) -> bool:
        x = len(board)
        y = len(board[0])
        for i in range(0,x,3):
            for j in range(0,y,3):
                if self.isValidSqr(board, i ,j) == False:
                    return False

        return True
                