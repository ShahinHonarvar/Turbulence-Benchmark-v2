def expand_around_center(s: str, left: int, right: int) -> set:
    palindromes = set()
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        palindrome = s[left:right + 1]
        if len(palindrome) >= 86:
            palindromes.add(palindrome)
        left -= 1
        right += 1
    return palindromes

def palindrome_of_length_at_least_n(s: str) -> set:
    s = ''.join([c for c in s if c.isalpha()]).lower()
    palindromes = set()
    for i in range(len(s)):
        odd_length_palindromes = expand_around_center(s, i, i)
        even_length_palindromes = expand_around_center(s, i, i + 1)
        palindromes.update(odd_length_palindromes)
        palindromes.update(even_length_palindromes)
    return palindromes