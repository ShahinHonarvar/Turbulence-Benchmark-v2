from itertools import combinations

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for length in range(4, len(s) + 1):
        for substring in combinations(s, length):
            substring = ''.join(substring)
            if all((char in alphabet for char in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes