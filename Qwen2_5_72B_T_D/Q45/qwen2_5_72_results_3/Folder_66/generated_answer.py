from itertools import permutations

def palindromes_between_indices(s):
    substring = s[:6]
    letter_counts = {}
    for letter in substring:
        if letter.isalpha():
            letter_counts[letter.lower()] = letter_counts.get(letter.lower(), 0) + 1
    possible_palindromes = set()
    for perm in permutations(letter_counts.items()):
        half = ''
        for letter, count in perm:
            half += letter * (count // 2)
        for i in range(len(half) + 1):
            candidate = half[:i] + (perm[i][0] if perm[i][1] % 2 != 0 else '') + half[i:][::-1]
            if len(candidate) >= 5:
                possible_palindromes.add(candidate)
    return possible_palindromes