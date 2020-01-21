from lib.basic_data_structures import ListNode


def reverse_linked_list(head: ListNode) -> ListNode:
    if not head:
        return head
    prev_node, curr_node, next_node = None, head, head.next
    while curr_node:
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
        if curr_node:
            next_node = next_node.next
    return prev_node


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print(reverse_linked_list(head))
