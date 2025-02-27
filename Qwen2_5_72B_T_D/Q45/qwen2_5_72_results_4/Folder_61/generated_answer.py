from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:8]
    letter_counts = {char: substring.count(char) for char in substring if char.isalpha()}
    potential_palindromes = set()
    for perm in permutations(letter_counts.items()):
        half = ''
        for char, count in perm:
            half += char * (count // 2)
        for i in range(len(half) + 1):
            candidate = half[:i] + (perm[i][0] if i < len(perm) and perm[i][1] % 2 != 0 else '') + half[i:][::-1]
            if len(candidate) >= 7:
                potential_palindromes.add(candidate.lower())
    return potential_palindromes