def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)

    def expand_around_center(left, right):
        while left >= 0 and right < n and (s[left] == s[right]):
            if right - left + 1 >= 25:
                palindromes.add(s[left:right + 1])
            left -= 1
            right += 1
    for i in range(n):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)
    return palindromes