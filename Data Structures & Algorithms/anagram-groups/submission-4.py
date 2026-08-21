class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            str = "".join(sorted(s))
            groups[str] = groups.get(str, [])
            groups[str].append(s)
        return list(groups.values())
