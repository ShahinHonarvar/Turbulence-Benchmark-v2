def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 29, len(s) + 1):
            substr = s[i:j]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes

def is_palindrome(s):
    return s == s[::-1] and all((c.isalpha() for c in s))