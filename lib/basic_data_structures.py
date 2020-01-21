class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if not self:
            return None
        s = str(self.val)
        curr = self.next
        while curr:
            s += '->' + str(curr.val)
            curr = curr.next
        return s
