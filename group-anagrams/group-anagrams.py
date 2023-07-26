from ast import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        val = defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            for letters in word:
                count[ord(letters)- ord("a")] += 1
            val[tuple(count)].append(word)
        return val.values()