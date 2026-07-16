class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        res = ""
        for i in range(n):
            res = res + str(len(strs[i])) + "#" + strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)
        i = 0
        while i < n:
            ind = i
            while s[ind].isdigit():
                ind += 1
            num = int(s[i : ind])
            ind += 1
            res.append(s[ind : ind + num])
            i = ind + num
        return res
            