def expand_around_center(s, left, right):
    length = 0
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        length += 2
        left -= 1
        right += 1
    return length - 2

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        max_len = max(len1, len2)
        if max_len >= 40:
            palindromes.add(s[i - (max_len - 1) // 2:i + max_len // 2 + 1].lower())
    return palindromes