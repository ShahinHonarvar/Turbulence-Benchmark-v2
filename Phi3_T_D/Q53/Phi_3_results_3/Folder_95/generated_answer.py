def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def expand_palindrome(left, right):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            left -= 1
            right += 1
        return s[left + 1:right]
    palindromes = set()
    for i in range(len(s)):
        pal1 = expand_palindrome(i, i)
        pal2 = expand_palindrome(i, i + 1)
        for pal in [pal1, pal2]:
            if len(pal) >= 35:
                palindromes.add(pal)
    return palindromes