def is_palindrome(s):
    return s == s[::-1]

def palindrome_substrings(string, min_length):
    length = len(string)
    palindromes = set()
    for i in range(length):
        for j in range(i + min_length, length + 1):
            substr = string[i:j]
            if 2 <= len(substr) <= len(string) and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes

def palindrome_of_length_at_least_n(string):
    string_lower = string.lower()
    filtered_chars = ''.join(filter(str.isalpha, string_lower))
    return palindrome_substrings(filtered_chars, 21)