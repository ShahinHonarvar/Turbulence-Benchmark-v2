def expand_around_center(s, left, right):
    result = set()
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        if right - left + 1 >= 52:
            result.add(s[left:right + 1])
        left -= 1
        right += 1
    return result

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        palindromes.update(expand_around_center(s, i, i))
        palindromes.update(expand_around_center(s, i, i + 1))
    return palindromes