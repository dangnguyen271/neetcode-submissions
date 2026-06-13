class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row handling
        for row in board:
            count = 0
            unique = len(set(row))
            for item in row:
                if item != ".":
                    count += 1
            if count >= unique:
                return False

        # Column handling
        for i in range(9):
            count = 0
            col = []
            for j in range(9):
                col.append(board[j][i])
                if board[j][i] != ".":
                    count +=1
            unique = len(set(col))
            if count >= unique:
                return False

        # Sub-box handling
        sub_boxes = [[] for i in range(9)]
        for i in range(9):
            for j in range(9):
                sub_boxes[(i // 3) * 3 + (j // 3)].append(board[i][j])

        for sub_box in sub_boxes:
            count = 0
            unique = len(set(sub_box))
            for item in sub_box:
                if item != ".":
                    count += 1
            
            if count >= unique:
                return False

        return True
                    
