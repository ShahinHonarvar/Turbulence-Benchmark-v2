def palindrome_of_length_at_least_n(s):

    def expand_around_center(left, right):
        length = 0
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            length = right - left + 1
            left -= 1
            right += 1
        return length
    palindromes = set()
    s = ''.join((c for c in s if c.isalpha())).lower()
    for i in range(len(s)):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        for length in (len1, len2):
            if length >= 52:
                palindromes.add(s[i:i + length])
    return palindromes