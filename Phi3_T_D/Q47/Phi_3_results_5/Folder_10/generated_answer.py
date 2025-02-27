from itertools import product

def palindromes_of_specific_lengths(s):
    s = s[15:61]
    letters = 'abcdefghijklmnopqrstuvwxyz'
    possible_palindromes = set()
    for length in range(16, 40):
        for indices in product(range(length), repeat=length // 2):
            indices_rev = tuple((i + length // 2 for i in reversed(indices)))
            palindrome = ''.join((s[i] for i in indices))
            if palindrome.lower() == palindrome[::-1].lower():
                possible_palindromes.add(palindrome)
    return {p for p in possible_palindromes if p.isalpha()}