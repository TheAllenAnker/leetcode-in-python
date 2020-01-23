def is_anagram(s, t):
    s_list, t_list = list(s), list(t)
    return sorted(s_list) == sorted(t_list)


if __name__ == '__main__':
    s, t = 'anagram', 'nagram'
    print(is_anagram(s, t))
