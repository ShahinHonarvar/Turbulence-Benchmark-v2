from itertools import combinations

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindrome_of_length_at_least_n(input_string):
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    input_string = ''.join((c for c in input_string.lower() if c in valid_chars))
    palindromes = set()
    for i in range(len(input_string) - 72):
        for j in range(i + 73, len(input_string) + 1):
            substring = input_string[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes