import math
from itertools import *
array= [10, 5, 20, 25, 15, 5, 5, 15, 3, 15, 5, 5, 15]#90
array=[10, 5, 20, 25, 15, 5, 5, 15] #60
def maxSubsetSumNoAdjacent1(array):
    if not len(array):
        return 0
    if len(array)==1:
        return array[0]
    indexer=range(len(array))
    index_combination=[temp for i in range(math.floor(len(array)/2),len(array)) for temp in list(combinations(indexer,i))]
    array_combination = [temp for i in range(math.floor(len(array) / 2), len(array)) for temp in list(combinations(array, i))]
    tracker={index_combination[i]:array_combination[i] for i in range(len(array_combination))}
    #filter out the ones in tracker
    updated_tracker={tup:tracker[tup] for tup in tracker if all(tup[i]+1!=tup[i+1] for i in range(len(tup)-1))}
    return max([sum(i) for i in updated_tracker.values()])
    print(updated_tracker)

#second implementation for above solution but this time we have a one liner
    #not really necessary because it will be disastrous
#so I have opted for a rather dynamic programming code that I have found online from one of the solutions
def maxSubsetSumNoAdjacent(array):
    currentMax,previousMax=0,0
    for number in array:
        previousMax,currentMax=currentMax,max(currentMax,previousMax+number)
    return currentMax











#problematic code since it doesn't make an optimization for the fact that you can trade off larger numbers for more space to aggregate smaller numbers and make a bigger one than the max value in the list.

# def checker(tracker):
#     i=0
#
#     while i < len(tracker)-1 and len(tracker):
#             lenset = list(sorted(tracker.keys()))
#             print("Caution1:", lenset, len(lenset))
#             if lenset[i]+1==lenset[i+1]:
#                 if tracker[lenset[i]]>tracker[lenset[i+1]]:
#                     print("Correction1", "Pop:", tracker[lenset[i+1]],"index:",lenset[i+1], "Compare:", tracker[lenset[i]],"index:",lenset[i])
#                     tracker.pop(lenset[i+1])
#
#                 # elif tracker[lenset[i]]<tracker[lenset[i+1]]:
#                 else:
#                     print('Correction2', "Pop:", tracker[lenset[i]],"index:",lenset[i], "Compare:", tracker[lenset[i+1]],"index:",lenset[i+1])
#                     tracker.pop(lenset[i])
#             print("Caution2:", len(lenset))
#             i+=1
#
#
#
#
#     print(True)

print(maxSubsetSumNoAdjacent(array))
denoms=  [5,1,3]
n= 9


def numberOfWaysToMakeChange(n, denoms, current_combination=[], array=[]):
    if n == 0:
        # If the combination is unique, add it to the array

        if len(current_combination)==0:return 1
        current_combination.sort()
        if current_combination not in array:
            array.append(current_combination)
        return
    if n < 0:

        return

    for i in denoms:
        numberOfWaysToMakeChange(n - i, denoms, current_combination + [i], array)
    print(array)
    return len(array)

print(numberOfWaysToMakeChange(n, denoms))

#this is a personal solution that makes use of the combinations_with_replacement() function
def numberOfWaysToMakeChange(n, denoms, temp=None, count=None):
    # think that numberOfWaysToMakeChange() function is combinations_with_replacement() function
    if temp is None: temp = []
    if count is None: count = 0

    if len(temp) == n:
        print("the fuck is this", temp, len(denoms))
        return 1 if not n else count
    for i in range(len(denoms)):
        temp.append(denoms[i])
        if sum(temp) == n:
            print(temp, count)
            count += 1
        count = numberOfWaysToMakeChange(n, denoms[i:], temp, count)
        temp.pop()

    print(count)
    return count
#the above code is essentially the same thing as the one liner

#oneliner solution
#return len([temp for i in range(1,n+1) for temp in list(combinations_with_replacement(denoms,i)) if sum(temp)==n])

#This is the powerset implementation I cooked up after working with combination, permutation and combination_with_replacement, I accidentally stumbled at the property
def powerset(array, temp=None, appender=None, length=None):
    if appender is None and temp is None:
        temp = []
        appender = [[]]
        length = len(array)
    if len(temp) == length:
        return appender
    for i in range(len(array)):

        temp.append(array[i])
        print("Array,", array)
        if temp not in appender:
            appender.append(temp[:])
        if array not in appender:
            appender.append(array[:])
        powerset(array[i + 1:], temp, appender, length)
        temp.pop()
    appender.sort(key=len)
    return appender
print(powerset([1,2,3,4,5]))

#beneath you shall find the inspiration for the above code

# def permutations(array, i=0, appender=[]):
#     indentation = '\t' * i  # Add i tabs for indentation
#
#     print(f"{indentation}Entering function with array: {array}, i: {i}, appender: {appender}")
#
#     if i == len(array):
#         print(f"{indentation}Base case reached with array: {array}")
#         appender.append(array[:])
#         print(f"{indentation}Appending to appender: {appender}")
#         return appender
#
#     j = i
#     while j < len(array):
#         print(f"{indentation}i: {i}, j: {j}")
#         print(f"{indentation}Before swapping: {array}")
#         array[i], array[j] = array[j], array[i]
#         print(f"{indentation}After swapping {array[i]} and {array[j]} at indices {i} and {j}: {array}")
#
#         # Recursive call with i incremented by 1
#         print(f"{indentation}Calling recursive function with array: {array}, i: {i + 1}")
#         permutations(array, i + 1, appender)
#
#         # Swap them back to revert the change
#         print(f"{indentation}Reverting swap of {array[i]} and {array[j]} at indices {i} and {j}")
#         array[i], array[j] = array[j], array[i]
#         print(f"{indentation}After reverting: {array}")
#
#         j += 1
#
#     print(f"{indentation}Exiting function with array: {array}, i: {i}, appender: {appender}")
#     return appender
#
# print(permutations([1, 2, 3]))

def combinations(array,k,temp=[],appender=[]):

    if len(temp)==k:
        appender.append(temp[:])
        print("Appender:",appender,'Temp:',temp)
        return appender
    for i in range(len(array)):
        print("Before append",i,temp)
        temp.append(array[i])
        print("After append and before call",i,temp)
        combinations(array[i+1:],k,temp,appender)
        print("After call and before pop",i,temp)
        temp.pop()
        print('After pop',i,temp)
    return appender

print(combinations([1,2,3],6))

def combinations_with_replacement(array,k,temp=[],appender=[]):

    if len(temp)==k:
        appender.append(temp[:])
        print("Appender:",appender,'Temp:',temp)
        return appender
    for i in range(len(array)):
        print("Before append",i,temp)
        temp.append(array[i])
        print("After append and before call",i,temp)
        combinations(array[i:],k,temp,appender)
        print("After call and before pop",i,temp)
        temp.pop()
        print('After pop',i,temp)
    return appender

print(combinations([1,2,3],6))
