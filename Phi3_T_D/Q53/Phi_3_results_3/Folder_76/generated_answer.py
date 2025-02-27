def expand_around_center(s, left, right):
    length = 0
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        left -= 1
        right += 1
        length += 1
    return length - 1

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        length = max(len1, len2)
        while length >= 137:
            palindrome = s[i - (length - 1) // 2:i + length // 2 + 1]
            if palindrome.isalpha():
                palindromes.add(palindrome)
            length -= 2
    return palindromes