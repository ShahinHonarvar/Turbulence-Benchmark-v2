from itertools import combinations

def palindromes_between_indices(text):
    sub_text = text[1:10].lower()
    letters = [char for char in sub_text if char.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for combo in combinations(letters, length):
            if is_palindrome(''.join(combo)):
                palindromes.add(''.join(combo))
    return palindromes

def is_palindrome(s):
    return s == s[::-1]