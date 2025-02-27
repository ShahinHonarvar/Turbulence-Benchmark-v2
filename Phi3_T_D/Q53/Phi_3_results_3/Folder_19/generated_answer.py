def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)

    def expand_around_center(left, right):
        while left >= 0 and right < n and (s[left] == s[right]):
            left -= 1
            right += 1
        return s[left + 1:right]
    palindromes = set()
    for i in range(n):
        for j in range(i + 22, n):
            substring = expand_around_center(i, j)
            if len(substring) >= 23:
                palindromes.add(substring)
    return palindromes