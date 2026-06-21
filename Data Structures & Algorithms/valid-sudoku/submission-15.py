class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # setup the cols, rows, squares for location and check every edge case to avoid the duplicate value we've seen

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        # looping each cols and rows and check edge case
        for c in range(9):
            for r in range(9):
                # check if have empty value
                if board[c][r] == ".":
                    continue 
                # check if we've seen this value before
                if (board[c][r] in cols[c] or
                    board[c][r] in rows[r] or 
                    board[c][r] in squares[(c// 3, r// 3)]):
                    return False
                # if not, update the board: add the current value to the board
                cols[c].add(board[c][r])
                rows[r].add(board[c][r])
                squares[(c // 3, r // 3)].add(board[c][r])

        return True
