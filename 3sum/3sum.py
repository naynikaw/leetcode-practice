class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        #nums = list(set(nums))
       #print(nums)
        nums = sorted(nums)
        n = len(nums)
        #print(nums)
        if n==3:
            if sum(nums)==0:
                result.append(nums)
                return result
        i = 0        
        while i <= n-3:
            j = i+1
            k = n-1
            #print(nums[i])
            while j<k:
                current_sum = nums[i]
                current_sum += nums[j]
                current_sum += nums[k]
                #print(current_sum)
                if current_sum == 0:
                    l = []
                    l.append(nums[i])
                    l.append(nums[j])
                    l.append(nums[k])
                    if l not in result:
                        result.append(l)
                    k -= 1
                    j += 1
                
                elif current_sum > 0:
                    k -= 1
                
                else:
                    j += 1
            i += 1
        return result