def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()

    def expand(center, left, right):
        while left >= 0 and right < n and (s[left] == s[right]):
            if right - left + 1 >= 70:
                palindromes.add(s[left:right + 1])
            left -= 1
            right += 1
    for i in range(n):
        expand(i, i, i)
        expand(i, i, i + 1)
    return palindromes