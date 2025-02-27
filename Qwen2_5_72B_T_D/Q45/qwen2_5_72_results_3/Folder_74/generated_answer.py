from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:7]
    letter_counts = {}
    for letter in substring:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    potential_palindromes = set()
    for perm in permutations(letter_counts.items()):
        half = ''
        for letter, count in perm:
            half += letter * (count // 2)
        if len(half) >= 3:
            for i in range(len(half)):
                palindrome = half[:i] + (half[i] if count % 2 else '') + half[i:][::-1]
                if len(palindrome) >= 6:
                    potential_palindromes.add(palindrome)
    return potential_palindromes