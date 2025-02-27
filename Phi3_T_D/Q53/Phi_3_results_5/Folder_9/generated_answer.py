def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()

    def expand_around_center(left, right):
        while left >= 0 and right < length and (s[left] == s[right]):
            if right - left + 1 >= 95:
                palindromes.add(s[left:right + 1])
            left -= 1
            right += 1
    for i in range(length):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)
    return palindromes