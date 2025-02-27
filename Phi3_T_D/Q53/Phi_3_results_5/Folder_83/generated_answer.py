from itertools import combinations

def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    potential_palindromes = set()
    for i in range(len(text)):
        for combo in combinations(range(len(text)), 60):
            substring = ''.join((text[j] for j in combo))
            if is_palindrome(substring):
                potential_palindromes.add(substring)
    return {palindrome for palindrome in potential_palindromes if palindrome.isalpha()}