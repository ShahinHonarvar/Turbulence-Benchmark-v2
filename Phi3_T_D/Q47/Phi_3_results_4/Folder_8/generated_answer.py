import re

def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(text):
    substring = text[17:73]
    clean_substring = re.sub('[^a-zA-Z]', '', substring)
    lower_substring = clean_substring.lower()
    palindromes = set()
    for i in range(len(lower_substring) - 50):
        substring = lower_substring[i:i + 51]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes