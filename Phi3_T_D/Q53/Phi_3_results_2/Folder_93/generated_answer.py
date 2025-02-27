def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result_set = set()

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha():
            if s[left] == s[right] and right - left + 1 >= 90:
                result_set.add(s[left:right + 1])
                left -= 1
                right += 1
            elif s[left] != s[right]:
                break
            else:
                left -= 1
                right += 1
    for i in range(len(s)):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)
    return result_set