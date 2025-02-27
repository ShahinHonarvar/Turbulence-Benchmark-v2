from itertools import permutations

def palindromes_between_indices(text):
    substring = text[0:8].lower()
    chars = ''.join(sorted(set(substring)))
    if len(chars) < 6:
        return set()
    palindromes = set((''.join(p) for p in permutations(chars, 6)))
    valid_palindromes = {palindrome for palindrome in palindromes if palindrome == palindrome[::-1]}
    return valid_palindromes