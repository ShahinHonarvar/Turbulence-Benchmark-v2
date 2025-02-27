def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result_set = set()
    s_length = len(s)

    def expand_center(left, right):
        while left >= 0 and right < s_length and (s[left] == s[right]):
            if right - left + 1 >= 46:
                result_set.add(s[left:right + 1])
            left -= 1
            right += 1
    for i in range(s_length):
        expand_center(i, i)
        expand_center(i, i + 1)
    return result_set