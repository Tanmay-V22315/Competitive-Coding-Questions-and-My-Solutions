class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter=0
        addends = []
        for i in nums:
            y=nums
            y[counter]=None
            compnum = target-i
            if compnum in y:
                addends.append(counter)
                addends.append(y.index(target-i))
                return addends
            else:
                counter+=1
                

