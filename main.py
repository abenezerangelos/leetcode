
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
#######ALGOEXPERT PROBLEMS FROM HERE ON OUT###########
#Algoexpert easy array problem
def twoNumberSum(array, targetSum):
    i = 1
    n = 0
    while i < len(array):
        if array[n] + array[i] == targetSum:
            return [array[n], array[i]]

        elif i == len(array) - 1:

            n += 1
            i = n

        i += 1
    return []


def isValidSubsequence(array, sequence):
    # Write your code here.

    arr = 0
    seq = 0
    while arr < len(array) and seq < len(sequence):
        if array[arr] == sequence[seq]:
            seq += 1

        arr += 1
    return seq == len(sequence)





def sortedSquaredArray(array):
    squared = []
    for item in array:
        squared.append(item * item)

    return sorted(squared)


def tournamentWinner(competitions, results):
    i = 0


    dicter = {}
    for pairs in competitions:
        if results[i] == 0:
            if pairs[1] in dicter:
                dicter[pairs[1]] += 1
            else:
                dicter[pairs[1]] = 1
        else:
            if pairs[0] in dicter:
                dicter[pairs[0]] += 1
            else:
                dicter[pairs[0]] = 1
        i += 1
    array = ["sth", 0]
    for item in dicter:
        if dicter[item] > array[1]:
            print(item, dicter[item])
            array[0] = item
            array[1] = dicter[item]

    return array[0]
#this is a trial version that doesn't work i wasn't approaching the problem the right way, but it was worth a shot
def nonConstructibleChange(coins):
    # Write your code here.
    j = 0
    i = j + 1
    coins.sort()
    container = [coins[0]]
    while j < len(coins) - 1:

        container.append(coins[i] + container[-1])
        print(container, j, i)
        if i == len(coins) - 1:
            j += 1
            i = j
            container.append(coins[j])
        i += 1

    j = 0
    i = j + 1
    while j < len(coins) - 1:

        container.append(coins[i] + coins[j])
        print(container, j, i)
        if i == len(coins) - 1:
            j += 1
            i = j
            container.append(coins[j])
        i += 1

    for item in range(2, max(container)):
        if len(container) == 0:
            print("Item:", item)
            return 1

        elif item not in container:
            print("Item:", item)
            return item


#this is a better and impoved solution to the nonConstructibleChange problem on AlgoExpert
def nonConstructibleChange(coins):
    coins.sort()
    change=0
    for coin in coins:
        if coin>change+1:
            return change+1
        change+=coin
    return change+1

# A lot of these solutions were either inspired from someone else or are outright solutions that were handed  by Mihaelescu
# although you shouldn't be heart broken or in despair because there are some gems that you come up once in a while, good job. Keep going
def threeNumberSum(array, targetSum):
    # Write your code here.
    j = 0
    result = []
    array.sort()
    for i in array:
        for j in array:
            if targetSum - i - j in array and i < j < targetSum - i - j:
                result += [[i, j, targetSum - i - j]]
    return result


def smallestDifference(arrayOne, arrayTwo):
    array = []
    for item in arrayOne:
        i = 0
        while True:
            if item + i in arrayTwo:
                array += [[item, item + i, i]]
                break
            elif item - i in arrayTwo:
                array += [[item, item - i, i]]
                break
            i += 1
    value = array[0][2]
    for num in range(len(array)):
        if array[num][2] < value:
            value = array[num][2]
            index = num
            print(num)
    return [array[index][0], array[index][1]]


def moveElementToEnd(array, toMove):
    mover = -1
    if toMove in array:

        for item in range(len(array)):
            while array[mover] == toMove and mover * -1 != len(array) - 1:
                print(mover, mover * -1, len(array))
                mover -= 1
            if item == mover + 1 + len(array):
                break
            elif array[item] == toMove:
                array[item], array[mover] = array[mover], array[item]

            print(array)

        return array
    else:
        return array

#This was a very good well-tested and very original and authentic solution to a very hard but intuitive problem, good job
def isMonotonic(array):
    i = 0
    j = i + 1
    n = 0
    m = 1

    while j < len(array) and m < len(array):
        print(i, j)
        if array[n] < array[m] and array[i] <= array[j]:
            i += 1
            j = i + 1
        elif array[n] > array[m] and array[i] >= array[j]:
            i += 1
            j = i + 1
        elif array[n] == array[m]:
            n += 1
            m += 1

        else:
            return False
    return True
#Binary Tree word problems on Algoexpert
#The solution provided here is one of the best solutions that was inspired by the comment sectino online on the Algoexpert website
#Regardless very intuitive and great job
def findClosestValueInBst(tree, target):
    head = tree.value
    while tree is not None:
        if abs(target - head) > abs(target - tree.value):
            head = tree.value
        if target < tree.value:
            tree = tree.left
        elif target > tree.value:
            tree = tree.right
        else:
            break
    return head

#this is a very bulky and inefficient attempt at solving this problem
def findClosestValueInBst(tree, target):
    # Write your code here.
    head = tree.value
    while target != head and (tree.left != None or tree.right != None):

        if tree.left != None and tree.right != None:

            if abs(target - head) < abs(target - tree.left.value) and abs(target - head) < (target - tree.right.value):
                if abs(target - tree.left.value) < abs(target - tree.right.value):
                    print(tree.value, "VALUEE1")
                    tree = tree.left
                else:
                    print(tree.value, "VALUEE2")
                    tree = tree.right
            else:
                if abs(target - tree.left.value) < abs(target - tree.right.value):
                    print(tree.value, "VALUEE3")
                    head = tree.left.value
                    tree = tree.left
                else:
                    print(tree.value, "VALUEE4")
                    head = tree.right.value
                    tree = tree.right
        elif tree.left != None:
            if abs(target - head) > abs(target - tree.left.value):
                print(tree.value, "VALUEE5")
                head = tree.left.value
                tree = tree.left
            else:
                print(head, "LEFT111111")
                return head
        elif tree.right != None:
            if abs(target - head) > abs(target - tree.right.value):
                print(tree.value, "VALUEE6.value")
                head = tree.right.value
                tree = tree.right
            else:
                print(head, "RIGHT22222")
                return head
        else:
            print("ERROR")
    print(target != head, (tree.left != None or tree.right != None), tree.left != None, tree.right != None)
    print(head, "OUT OF LOOOP33333333")
    return head


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#This took me quite a while but it wasn't supposed to. I should have taken short breaks and got back to it again but i wasted too much time.
#I should have probably played chess or do a puzzle, then read something. Then get right back to it.
# this code is for the IS sub sequence, this code is both memory and time efficient. It might be the most efficient thing, I have done so far.
def isSubsequence(self, s: str, t: str) -> bool:
    array = []
    if s in t:
        print(s, t)
        return True
    i = 0
    for letter in s:
        dif = t.count(letter) - s.count(letter)
        if dif > 0:
            t = t.replace(letter, '', dif)
            print("DEBUGGGGGER!!!", dif)
        print(dif, letter, t.count(letter))
        if letter in t:
            ind = t.index(letter)
            t = t.replace(letter, '', 1)

            array.append(ind)
            print(array)
        else:
            print(False, 3333333333333)
            return False

    if len(s) != len(array):
        return (False, 11111111111)
    print(sorted(array))
    if array == sorted(array):
        print(True)

        return True
    else:
        print(False, 222222222222)
        print(array)
        return False


