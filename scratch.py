# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# x=ListNode(1,ListNode(4,ListNode(5)))
# print(x.next.val)
# array=[1,15,8,5,3,9,10,-1]
#
#
# #solving the problem of creating a LinkedList with a certain amount of nodes either recursively or using loops
# #probably using recursion since It seems to be easier that way
# saver=y=ListNode(array[0])
# print("whatever")
# for i in array[1:]:
#     y.next=ListNode(i)
#     y=y.next
#
# print(saver.val,saver.next.val,saver.next.next.val,saver.next.next.next.val,saver.next.next.next.next.val,saver.next.next.next.next.next.val)
# print("DEBUG")
#
#
#
#
#
#
#
#
#
#
# #convert a ListNode to array
#
#
#
#
#
#
# #converting an array to a ListNode
# store=y = ListNode(array[0])
#
# for i in array[1:]:
#     y.next = ListNode(i)
#     y = y.next
#     print(y.val)
# print(store)
#
#
# #recursively tending to this problem
# #reserved for a future date
#
#
#
# #how to look for the median in an array:
#
# a=[1,2,3,4,10,2,5,6,7,8,9]
# if len(a)%2==0:
#     print(a[int(len(a)/2)])
# else:
#     print((a[int((len(a)/2))]))
# a.reverse()
# print(a)
# a.sort(reverse=True)
# print(a)
# z=[7,1]
# arr=[7]
# print(z[z.index(min(z)):])
# print(max(arr[:arr.index(min(arr))+1]),"What")
# print(z[:1].remove(z[0]))
# new=[7,6,5,3,1,2,0,3]
# anotha=[1,2,5,7,0,8]
# mod=[1,2,3,5,0]
#
# s=[]
# if s[:]==None:
#     print(True)
# else:
#     print(s[:])
#     print(False)
#
#
# print(bin(1),bin(2),bin(10),bin(255),bin(32))
#
#
#
#
# word=["a","b","c"]
# words=str(word)
# print(type(words))
# letter=(''.join(i) for i in word)
# lister=''.join(letter)
# print(lister)
# stringer="aberdeen"
# print(stringer.removeprefix("ab"))
#
# phrase=["11111001010","11100010",'111010101010']
# letters=f"{str(f'{i}' for i in word)}"
# print(1%2)
# def combinations(iterable, r):
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield tuple(pool[i] for i in indices)
# print(list(combinations([1,2,3,4,5,6,7,8],3)))
def my_decorator(func,item):
    def wrapper():
        print("Something is happening before the function is called.")
        func(item)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello(item):
    print(f"{item}")
word="Hello may"
say_hello(word)
def trial(item):
    def temp():
        i=item+2
        return i
    return []




