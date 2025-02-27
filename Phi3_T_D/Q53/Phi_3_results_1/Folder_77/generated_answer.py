def palindrome_of_length_at_least_n(s):
    results = set()

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            if right - left + 1 >= 149:
                results.add(s[left:right + 1])
            left -= 1
            right += 1
    for i in range(len(s)):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)
    return results