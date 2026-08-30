class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedmap = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            sortedmap[sortedS].append(s)

        return list(sortedmap.values())