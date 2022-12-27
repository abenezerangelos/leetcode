class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
x=ListNode(1,ListNode(4,ListNode(5)))
print(x.next.val)
array=[1,15,8,5,3,9,10,-1]


#solving the problem of creating a LinkedList with a certain amount of nodes either recursively or using loops
#probably using recursion since It seems to be easier that way
saver=y=ListNode(array[0])
print("whatever")
for i in array[1:]:
    y.next=ListNode(i)
    y=y.next

print(saver.val,saver.next.val,saver.next.next.val,saver.next.next.next.val,saver.next.next.next.next.val,saver.next.next.next.next.next.val)
print("DEBUG")

array.sort()
print(array)


y=[]
print(y[0])





#convert a ListNode to array






#converting an array to a ListNode
# store=ListNode()
# i=0
# j=1
# lister=ListNode()
# store.val=array[i]
# store.next=ListNode(array[j],lister)
# i+=1
# j+=1
# while j<len(array):
#     lister.val = array[i]
#     lister.next = ListNode(array[j])
#     lister = lister.next
#     i+=1
#     j+=1
#     print(j,len(array))
# print(store.val, store.next.val,store.next.next.val,store.next.next.next.val,"!!!!!!!")
#recursively tending to this problem