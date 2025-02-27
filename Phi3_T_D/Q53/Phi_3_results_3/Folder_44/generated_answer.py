def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for length_limit in range(89, len(s) - i + 1):
            substr = s[i:i + length_limit]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes