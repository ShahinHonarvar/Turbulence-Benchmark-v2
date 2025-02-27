def expand(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        if right - left + 1 >= 119:
            palindromes.append(s[left:right + 1])
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(s):
    for i in range(len(s)):
        expand(s, i, i)
        expand(s, i, i + 1)
    return {p for p in palindromes if p.isalpha()}