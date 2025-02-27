def is_palindrome(s):
    return s.lower() == s[::-1].lower() and all((c.isalpha() for c in s))

def all_substrings(s):
    length = len(s)
    return [s[i:j] for i in range(length) for j in range(i + 1, length + 1)]

def palindrome_of_length_at_least_n(input_string):
    n = 42
    palindromes = set()
    for substr in all_substrings(input_string):
        if len(substr) >= n and is_palindrome(substr):
            palindromes.add(substr.lower())
    return palindromes