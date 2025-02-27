from collections import defaultdict
    from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(check):
        return check == check[::-1]
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    letter_count = defaultdict(int)
    for letter in letters:
        letter_count[letter] += 1
    possible_chars = ''.join([c * (n // 2) for c, n in letter_count.items()])
    palindromes = set()
    for perm in permutations(possible_chars):
        half = ''.join(perm)
        full = half + (max([c for c, n in letter_count.items() if n % 2 == 1], default='') + half[::-1])
        if is_palindrome(full) and len(full) >= 4:
            palindromes.add(full)
    return palindromes