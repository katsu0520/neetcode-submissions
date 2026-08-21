class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            str = "".join(sorted(strs[i]))
            groups[str] = groups.get(str, [])
            groups[str].append(strs[i])
        return list(groups.values())
