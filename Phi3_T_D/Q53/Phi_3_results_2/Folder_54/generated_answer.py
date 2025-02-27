def extend_palindrome(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        left -= 1
        right += 1
    return s[left + 1:right]

def palindrome_of_length_at_least_n(s):
    set_palindromes = set()
    s_lower = s.lower()
    for i in range(len(s)):
        palindromes = set()
        for candidate in (extend_palindrome(s_lower, i, i), extend_palindrome(s_lower, i, i + 1)):
            if len(candidate) > 73:
                set_palindromes.add(candidate)
            palindromes.add(candidate)
        if len(palindromes.difference(set_palindromes)) > 0:
            set_palindromes.update(palindromes)
    return set_palindromes