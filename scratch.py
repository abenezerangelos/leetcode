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








#convert a ListNode to array






#converting an array to a ListNode
store=y = ListNode(array[0])

for i in array[1:]:
    y.next = ListNode(i)
    y = y.next
    print(y.val)
print(store)


#recursively tending to this problem