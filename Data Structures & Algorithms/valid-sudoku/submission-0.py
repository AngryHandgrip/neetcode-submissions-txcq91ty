class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)
        for i, row in enumerate(board):
            for j, s in enumerate(row):
                if s == '.':
                    continue
                if s in rows[i] or s in cols[j] or s in squares[(i//3, j//3)]:
                    return False
                rows[i].add(s)
                cols[j].add(s)
                squares[(i//3, j//3)].add(s)
        return True