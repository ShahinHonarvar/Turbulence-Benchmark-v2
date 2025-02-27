def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        yield (left, right)
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for left, right in expand_around_center(s, i, i):
            odd_pal = s[left:right + 1]
            if len(odd_pal) >= 59:
                palindromes.add(odd_pal)
        for left, right in expand_around_center(s, i, i + 1):
            even_pal = s[left:right + 1]
            if len(even_pal) >= 59:
                palindromes.add(even_pal)
    return palindromes