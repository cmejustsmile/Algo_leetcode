class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newdict= {}
        answers = [0,0]
        for i in range(0, len(nums)):
            if nums[i] in newdict:
                newdict[nums[i]].insert(-1,i)
            else:
                newdict[nums[i]] = [i]

        tmpdict = newdict.copy()

        for key in newdict.keys():
            if key in tmpdict and len(tmpdict[key]) == 0:
                tmpdict.pop(key)
                continue

            idx = tmpdict[key].pop()

            if target-key in tmpdict:
                if len(tmpdict[target-key]) == 0:
                    tmpdict.pop(target-key)
                    continue
                idx2 = tmpdict[target-key].pop()

                if idx2 < idx:
                    answers[0] = idx2
                    answers[1] = idx
                else:
                    answers[0] = idx
                    answers[1] = idx2
                return answers

        return answers