def expand_around_center(s, left, right, case_insensitive):
    if not case_insensitive:
        s = s.lower()
    while left >= 0 and right < len(s) and (s[left] == s[right]):
        left -= 1
        right += 1
    return s[left + 1:right]

def palindrome_of_length_at_least_n(s, min_length=67, case_insensitive=True):
    palindromes = set()
    for i in range(len(s)):
        palindrome1 = expand_around_center(s, i, i, case_insensitive)
        palindrome2 = expand_around_center(s, i, i + 1, case_insensitive)
        for palindrome in [palindrome1, palindrome2]:
            if len(palindrome) >= min_length:
                palindromes.add(palindrome)
    return palindromes