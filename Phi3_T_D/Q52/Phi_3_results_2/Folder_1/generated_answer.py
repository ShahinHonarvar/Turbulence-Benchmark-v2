def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(s):
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s_lower) - 26):
        substr = s_lower[i:i + 27]
        if all((c.isalpha() for c in substr)) and is_palindrome(substr):
            palindromes.add(substr.lower())
    return palindromes