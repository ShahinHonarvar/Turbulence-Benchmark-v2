from itertools import combinations

def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 146):
        for j in range(i + 147, len(string) + 1):
            substr = string[i:j]
            if all((c.isalpha() for c in substr)):
                if is_palindrome(substr):
                    palindromes.add(substr)
    return palindromes