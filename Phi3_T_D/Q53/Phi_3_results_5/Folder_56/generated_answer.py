def expansion_center(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        left -= 1
        right += 1
    return s[left + 1:right]

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        odd_length_palindrome = expansion_center(s, i - 1, i + 1)
        even_length_palindrome = expansion_center(s, i - 1, i)
        if len(odd_length_palindrome) >= 84 and all((c.isalpha() for c in odd_length_palindrome)):
            palindromes.add(odd_length_palindrome)
        if len(even_length_palindrome) >= 84 and all((c.isalpha() for c in even_length_palindrome)):
            palindromes.add(even_length_palindrome)
    return palindromes