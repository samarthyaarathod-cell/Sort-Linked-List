# Complete Python Program to Sort a Linked List in Ascending Order
# Using Merge Sort Algorithm (O(n log n) Time Complexity)

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:

    # Function to sort linked list
    def sortList(self, head):

        # Base case
        if not head or not head.next:
            return head

        # Step 1: Find middle of linked list
        middle = self.getMiddle(head)
        nextToMiddle = middle.next

        # Split the list into two halves
        middle.next = None

        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(nextToMiddle)

        # Step 3: Merge sorted halves
        sortedList = self.merge(left, right)

        return sortedList

    # Function to merge two sorted linked lists
    def merge(self, left, right):

        dummy = ListNode(0)
        tail = dummy

        while left and right:

            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        # Add remaining nodes
        if left:
            tail.next = left

        if right:
            tail.next = right

        return dummy.next

    # Function to find middle node
    def getMiddle(self, head):

        if not head:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# Function to create linked list
def createLinkedList(arr):

    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# Function to print linked list
def printLinkedList(head):

    current = head

    while current:
        print(current.val, end=" ")
        current = current.next

    print()


# ---------------- MAIN PROGRAM ----------------

solution = Solution()

# Example 1
arr1 = [4, 2, 1, 3]

head1 = createLinkedList(arr1)

sortedHead1 = solution.sortList(head1)

print("Sorted Linked List 1:")
printLinkedList(sortedHead1)


# Example 2
arr2 = [-1, 5, 3, 4, 0]

head2 = createLinkedList(arr2)

sortedHead2 = solution.sortList(head2)

print("Sorted Linked List 2:")
printLinkedList(sortedHead2)


# Example 3
arr3 = []

head3 = createLinkedList(arr3)

sortedHead3 = solution.sortList(head3)

print("Sorted Linked List 3:")
printLinkedList(sortedHead3)