def palindrome_of_length_at_least_n(s):

    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            if right - left + 1 >= 3:
                yield s[left:right + 1]
            left -= 1
            right += 1
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for palindrome in expandAroundCenter(i, i):
            palindromes.add(palindrome)
        for palindrome in expandAroundCenter(i, i + 1):
            palindromes.add(palindrome)
    return palindromes