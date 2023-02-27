import sys
sys.path.insert(1, '../')
from assertEquals import assertEquals


def middleNodeNON(ll):
    return ll[len(ll)//2:]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(self, head):
    slow = fast = head
    #tant que fast ou fast + 1 != None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def populate(data):
    tail = head = ListNode(data[0])
    for x in data[1:]:
        tail.next = ListNode(x)
        tail = tail.next


tests = [
[[1,2,3,4,5],[3,4,5]],
[[1,2,3,4,5,6],[4,5,6]]
]
for i in tests:
    llist = populate(i[0])
    print(assertEquals(middleNode(llist, llist.head),i[1]))