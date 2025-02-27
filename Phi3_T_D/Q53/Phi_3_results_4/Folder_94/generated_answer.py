def palindrome_of_length_at_least_n(s):

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left].isalpha() and s[right].isalpha()):
            if s[left].lower() == s[right].lower():
                yield s[left:right + 1]
            else:
                break
            left -= 1
            right += 1
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for pal in expand_around_center(i, i):
            if len(pal) >= 41:
                palindromes.add(pal)
        for pal in expand_around_center(i, i + 1):
            if len(pal) >= 41:
                palindromes.add(pal)
    return palindromes