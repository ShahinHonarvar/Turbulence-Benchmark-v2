def is_palindrome(s):
    return s == s[::-1]

def filter_palindromes(s, start, end, min_len, max_len):
    palindromes = set()
    for length in range(min_len, max_len + 1):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring.lower()):
                palindromes.add(substring.lower())
    return palindromes

def palindromes_of_specific_lengths(s):
    return filter_palindromes(s, 16, 77, 43, 47)