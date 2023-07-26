class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ret=[]
        j=k
        for x in nums:
            if x in count:
                count[x]+=1
            else:
                count[x]=0
        while(k>0):
            maximumKey = max(count, key=count.get)
            print(count)
            ret.append(maximumKey)
            count.pop(maximumKey)
            k-=1
        return ret