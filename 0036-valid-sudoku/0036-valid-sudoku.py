class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if self.validRow(board) == True and self.validColumn(board) == True and self.validSquare(board) == True:
            return True
        return False
    
    def validRow(self, board):
        for i in range(len(board)):
            if self.validList(board[i]) == False:
                return False
        return True

    def validColumn(self,board):
        for i in range(len(board)):
            column = [row[i] for row in board]
            if self.validList(column) == False:
                return False
        return True
    
    def validSquare(self, board):
        square = []
        for i in [0,3,6]:
            for j in [0,3,6]:
                square = []
                for x in range(3):
                    for y in range(3):
                        square.append(board[i + x][j + y])
                if self.validList(square) == False:
                    return False
        return True

    def validList(self, list):
        list2 = [i for i in list if i != '.']
        return len(set(list2)) == len(list2)