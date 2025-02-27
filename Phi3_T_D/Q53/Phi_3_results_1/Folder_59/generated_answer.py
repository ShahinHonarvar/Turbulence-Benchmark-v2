def find_substrings(s, l):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if len(s[i:j]) == l]

def is_palindrome(s):
    return s == s[::-1] and s.isalpha()

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    unique_palindromes = set()
    for length in range(20, len(s) + 1):
        substrings = find_substrings(s, length)
        for substring in substrings:
            if is_palindrome(substring):
                unique_palindromes.add(substring.upper())
    return unique_palindromes