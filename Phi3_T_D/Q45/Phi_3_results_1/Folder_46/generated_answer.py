from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10]
    counter = Counter(substring.lower())
    letter_count = sum((count for count in counter.values() if count >= 6))
    if letter_count < 6:
        return set()
    available_letters = ''.join((letter for letter, count in counter.items() if count >= 6))
    half_palindrome = ''.join((letter * (count // 2) for letter, count in counter.items() if count >= 6))
    fully_palindromic = {half_palindrome}
    for _ in range(letter_count // 2 - len(half_palindrome)):
        new_permutations = set((''.join(p) for p in permutations(available_letters, 1)))
        fully_palindromic.update((''.join([letter, x, letter]) for palindrome in fully_palindromic for letter in set(available_letters) for x in new_permutations if ''.join([letter, x, letter]) == ''.join([letter, x, letter])[::-1]))
    return {''.join(p) for p in permutations(half_palindrome, 3) + permutations(half_palindrome + half_palindrome[::-1], 3)}