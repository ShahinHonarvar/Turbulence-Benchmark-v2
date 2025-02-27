from collections import Counter

def palindromes_between_indices(s):
    substring = s[1:5]
    counter = Counter(substring.lower())
    odd_counts = sum((1 for count in counter.values() if count % 2 != 0))
    possible_palindromes = set()
    if odd_counts <= 1:
        for length in range(4, len(substring) + 1, 2):
            for candidate in set(permutations(substring, length)):
                if candidate.lower() == candidate[::-1].lower():
                    possible_palindromes.add(''.join(candidate))
    return possible_palindromes