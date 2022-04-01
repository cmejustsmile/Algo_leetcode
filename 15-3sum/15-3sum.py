class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N, result = len(nums), []
        i = 0
        while i < N:
            j, k = i+1, N-1
            while j<k:
                sum =nums[i]+nums[j]+nums[k]
                if sum == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    while j<N-1 and nums[j] == nums[j+1] :
                        j+=1
                    while k>-1 and nums[k] == nums[k-1] :
                        k-=1
                    j+=1
                    k-=1
                elif sum > 0 :
                    while k > -1 and nums[k] == nums[k - 1]:
                        k -= 1
                    k -=1
                else :
                    while j<N-1 and nums[j] == nums[j+1] :
                        j+=1
                    j+=1

            while i<N-1 and nums[i]==nums[i+1]:
                i+=1
            i+=1


        return result