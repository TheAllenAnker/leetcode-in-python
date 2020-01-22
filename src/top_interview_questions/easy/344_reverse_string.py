def reverse_string(s):
    if not s or len(s) < 0:
        return
    low, high = 0, len(s) - 1
    while low < high:
        s[low], s[high] = s[high], s[low]
        low += 1
        high -= 1


if __name__ == '__main__':
    motto = 'I would rather die with passion.'
    l1 = list(motto)
    reverse_string(l1)
    print(l1)