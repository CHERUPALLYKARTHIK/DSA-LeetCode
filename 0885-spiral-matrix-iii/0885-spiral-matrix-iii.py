class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [[rStart, cStart]]
        if rows * cols == 1:
            return res
            
        r, c = rStart, cStart
        steps = 1
        
        while len(res) < rows * cols:
            # Move East
            for _ in range(steps):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            
            # Move South
            for _ in range(steps):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            
            steps += 1
            
            # Move West
            for _ in range(steps):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            
            # Move North
            for _ in range(steps):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            
            steps += 1
            
        return res