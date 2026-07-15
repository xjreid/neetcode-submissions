class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        n = len(strs)
        for i in range(1, n):
            size = len(pre)
            comp = strs[i]
            compsize = len(comp)
            good = [];
            for j in range(size):
                if j > compsize - 1:
                    break
                if pre[j] != comp[j]:
                    break
                good.append(pre[j])
            pre = "".join(good);
            if pre == "":
                return pre
        return pre