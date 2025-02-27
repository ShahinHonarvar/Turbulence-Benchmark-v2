from itertools import permutations

def palindromes_between_indices(s):
    substring = s[7:10]
    letter_counts = {}
    for char in substring:
        if char.isalpha():
            char = char.lower()
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    letters = ''.join((char * count for char, count in letter_counts.items()))
    palindromes = set()
    for perm in permutations(letters):
        for i in range(len(perm)):
            for j in range(i + 2, len(perm) + 1):
                candidate = perm[i:j]
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes