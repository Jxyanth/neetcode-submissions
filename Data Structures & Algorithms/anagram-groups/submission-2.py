from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict=defaultdict(list)
        for i in strs:
            b="".join(sorted(i))  
            mydict[b].append(i)
        
        return list(mydict.values())