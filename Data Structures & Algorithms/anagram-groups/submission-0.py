class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        res.append([strs[0]])
        n = len(strs)
        for i in range(1, n):
            size = len(res)
            curr = Counter(strs[i])
            good = False;
            for j in range(size):
                if Counter(res[j][0]) == curr:
                    res[j].append(strs[i])
                    good = True
                    break
            if not good:
                res.append([strs[i]])
        return res
        