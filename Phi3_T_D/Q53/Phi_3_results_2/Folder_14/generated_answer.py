def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)

    def is_valid_char(ch):
        return ch.isalpha() and 32 <= ord(ch) <= 122

    def expand_at(left, right):
        while left >= 0 and right < n and is_valid_char(s[left]) and is_valid_char(s[right]) and (s[left] == s[right]):
            left -= 1
            right += 1
        if right - left - 1 >= 13:
            return (s[left + 1:right], left + 1, right - 1)
        return (None, -1, -1)
    for i in range(n):
        for j in (0, 1):
            pal, left, right = expand_at(i, i + j)
            if pal:
                palindromes.add(pal)
    return palindromes