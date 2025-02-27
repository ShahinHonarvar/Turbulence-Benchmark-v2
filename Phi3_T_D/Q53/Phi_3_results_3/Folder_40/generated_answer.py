def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()

    def expand_around_center(left, right):
        while left >= 0 and right < n and (s[left] == s[right]):
            palindrome = s[left:right + 1]
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
            left -= 1
            right += 1
    for i in range(n):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)
    return palindromes