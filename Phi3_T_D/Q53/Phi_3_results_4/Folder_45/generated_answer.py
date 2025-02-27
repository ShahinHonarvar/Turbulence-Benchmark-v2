def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result_set = set()
    length = len(s)

    def expand_around_center(left, right):
        while left >= 0 and right < length and (s[left] == s[right]):
            palindrome = s[left:right + 1]
            if len(palindrome) >= 47:
                result_set.add(palindrome)
            left -= 1
            right += 1
    for i in range(length):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)
    return result_set