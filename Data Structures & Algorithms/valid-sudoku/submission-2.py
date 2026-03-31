class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(0, 9):
            st = set()
            for col in range(0, 9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in st:
                    return False
                st.add(board[row][col])

        for row in range(0, 9):
            st = set()
            for col in range(0, 9):
                if board[col][row] == ".":
                    continue
                elif board[col][row] in st:
                    return False
                st.add(board[col][row])
        
        st_1 = set()
        st_2 = set()
        st_3 = set()

        for row in range(0, 3):
            for col in range(0, 3):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in st_1:
                    return False
                st_1.add(board[row][col])

            for col in range(3, 6):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in st_2:
                    return False
                st_2.add(board[row][col])

            for col in range(6, 9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in st_3:
                    return False
                st_3.add(board[row][col])

        st_1.clear()
        st_2.clear()
        st_3.clear()

        for row in range(3, 6):
            for col in range(0, 3):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in st_1:
                    return False
                st_1.add(board[row][col])

            for col in range(3, 6):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in st_2:
                    return False
                st_2.add(board[row][col])

            for col in range(6, 9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in st_3:
                    return False
                st_3.add(board[row][col])

        st_1.clear()
        st_2.clear()
        st_3.clear()

        for row in range(6, 9):
            for col in range(0, 3):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in st_1:
                    return False
                st_1.add(board[row][col])

            for col in range(3, 6):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in st_2:
                    return False
                st_2.add(board[row][col])

            for col in range(6, 9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in st_3:
                    return False
                st_3.add(board[row][col])


        return True