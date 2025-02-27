def is_palindrome(s):
    return s == s[::-1]

def filter_palindromes(s, start, end, min_length, max_length):
    return {s[i:j + 1] for i in range(start, end + 1) for j in range(i, end + 1) if min_length <= j - i + 1 <= max_length and is_palindrome(s[i:j + 1]) and s[i:j + 1].isalpha()}

def palindromes_of_specific_lengths(s):
    return filter_palindromes(s.lower(), 35, 88, 24, 33)