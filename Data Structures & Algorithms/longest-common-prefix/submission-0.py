class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strings = sorted(strs)

        for i in range(min(len(strings[0]),len(strings[-1]))):
            if strings[0][i] != strings [-1][i]:
                return strings[0][:i]
        
        return strings[0]