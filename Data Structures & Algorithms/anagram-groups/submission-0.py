class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs: # for every string in list of strings
            count = [0] * 26
            for c in s: # for every char in string from ^
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)   #must use a tuple since you need a lists and no mutation  

        return list(res.values() )     