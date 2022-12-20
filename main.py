
nums = [1,2,3,4]
#Output: [1,3,6,10]

def runningSum(self, nums) :
    array = [0]
    for i in nums:
        array.append(i + array[-1])
        print(array)
    array.remove(0)
    print(array)
    return array

#pivot index solution for leetcode 75 challenge
class Solution:
    def pivotIndex(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            print(i)
            print(i - 1)
            print(len(nums) - 1)

            if sum(nums[0:i]) == sum(nums[i + 1:len(nums)]):
                return i
            i += 1
        return -1
#String problem leetcode


def isIsomorphic(self, s: str, t: str) -> bool:
        i = 0

        dictionary = {}
        while i < len(s):
            dictionary[s[i]] = t[i]
            i += 1

        n = 0
        for letter in t:
            if letter != dictionary[s[n]] or list(dictionary.values()).count(letter) > 1:
                print(letter != dictionary[s[n]])
                print(list(dictionary.values()).count(letter) > 1)
                print(letter)
                return False
            n += 1

        print(dictionary)
        return True