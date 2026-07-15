class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqmap = Counter(list(s))
        for ch in t:
            if freqmap.get(ch) is None:
                return False;
            freqmap[ch] -= 1
            if freqmap[ch] == 0:
                del freqmap[ch];
        if freqmap:
            return False;
        return True;
        