def palindrome_of_length_n(s):

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            left -= 1
            right += 1
        return s[left + 1:right]
    palindromes = set()
    for i in range(len(s)):
        palindromes.add(expand_around_center(i, i))
        if i + 1 < len(s):
            palindromes.add(expand_around_center(i, i + 1))
    return {p for p in palindromes if len(p) == 80 and p.isalpha()}