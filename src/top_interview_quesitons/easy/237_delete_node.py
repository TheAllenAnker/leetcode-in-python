from lib.basic_data_structures import ListNode


def delete_node(node: ListNode):
    node.val = node.next.val
    node.next = node.next.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    delete_node(head)
    print(head)
