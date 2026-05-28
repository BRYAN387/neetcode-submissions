class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if length of strings arent =, then not anagram
            return False

        countS, countT = {}, {} #create hashmap

        for i in range(len(s)): # Only need to iterate over s, since we know they are equal lengths^
            countS[s[i]] = 1 + countS.get(s[i], 0) #counting the occurences of each character in string s
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        return countS == countT
