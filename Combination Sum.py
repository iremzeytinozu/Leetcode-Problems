class Solution(object):
    def combinationSum(self, candidates, target):
        
        result = []

        def dfs(i, curr, total):
            if total == target:
                result.append(curr[:]) # listenin kopyasini aldik (curr.copy())
                return 

            if i >= len(candidates) or total > target:
                return 

            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])

            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return result