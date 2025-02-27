from itertools import combinations

def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(string):
    substring_len = 475
    string = string.lower()
    palindromes = set()
    for substr_indices in combinations(range(len(string) - substring_len + 1), substring_len // 2):
        substr = string[min(substr_indices):max(substr_indices) + substring_len]
        if is_palindrome(substr):
            palindromes.add(substr)
    return palindromes