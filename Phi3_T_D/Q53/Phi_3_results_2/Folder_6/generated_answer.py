def expand_around_center(s, left, right):
    palindromes = set()
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        if right - left + 1 >= 22:
            palindromes.add(s[left:right + 1])
        left -= 1
        right += 1
    return palindromes

def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for i in range(len(s)):
        result.update(expand_around_center(s, i, i))
        result.update(expand_around_center(s, i, i + 1))
    return result