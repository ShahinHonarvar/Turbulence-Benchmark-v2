def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def expand(left, right, result):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            if right - left + 1 >= 24:
                result.add(s[left:right + 1])
            left -= 1
            right += 1
    palindromes = set()
    for i in range(len(s)):
        expand(i, i, palindromes)
        expand(i, i + 1, palindromes)
    return palindromes