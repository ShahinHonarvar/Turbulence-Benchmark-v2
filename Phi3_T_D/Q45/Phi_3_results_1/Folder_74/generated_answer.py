from itertools import permutations

def palindromes_between_indices(s):
    range_s = s[1:7]
    unique_chars = set((c.lower() for c in range_s if c.isalpha()))
    palindrome_candidates = []
    for length in range(6, len(unique_chars) + 1):
        for candidate in permutations(unique_chars, length):
            candidate_string = ''.join(candidate)
            if candidate_string == candidate_string[::-1]:
                palindrome_candidates.append(candidate_string)
    return set(palindrome_candidates)