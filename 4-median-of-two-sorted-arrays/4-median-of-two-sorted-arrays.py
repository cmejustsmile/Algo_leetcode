class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total = len(nums1) + len(nums2)
        cnt = 0
        ans = ans_p = 0

        i = j = 0
        
        if total == 1:
            if len(nums1) > 0 :
                return nums1[0]
            else:
                return nums2[0]
        
        while True:
            if cnt >= total / 2 + 1:
                if total % 2 == 0:
                    return (ans_p + ans) / 2
                else:
                    return ans_p

            ans_p = ans
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    ans = nums1[i]
                    i += 1
                else:
                    ans = nums2[j]
                    j += 1
                cnt += 1
            elif i < len(nums1):
                ans = nums1[i]
                i += 1
                cnt += 1
            elif j < len(nums2):
                ans = nums2[j]
                j += 1
                cnt += 1
            else:
                break
            
            

        return 0
  
        