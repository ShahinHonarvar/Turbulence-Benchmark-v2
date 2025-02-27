def palindrome_of_length_at_least_n(s):

    def expand_around_center(left, right):
        result = set()
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()) and (right - left + 1 >= 80):
            result.add(s[left:right + 1])
            left -= 1
            right += 1
        return result
    palindromes = set()
    for i in range(len(s)):
        palindromes |= expand_around_center(i, i)
        if i < len(s) - 1 and s[i] == s[i + 1]:
            palindromes |= expand_around_center(i, i + 1)
    return palindromes