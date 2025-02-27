def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def expand_around_center(left, right):
        result = set()
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            palindrome = s[left:right + 1]
            if len(palindrome) >= 59:
                result.add(palindrome)
            left -= 1
            right += 1
        return result
    palindromes = set()
    for i in range(len(s)):
        palindromes |= expand_around_center(i, i)
        palindromes |= expand_around_center(i, i + 1)
    return palindromes