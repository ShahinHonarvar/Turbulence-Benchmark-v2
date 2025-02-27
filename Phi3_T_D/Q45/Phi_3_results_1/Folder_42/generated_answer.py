from itertools import permutations

def palindromes_between_indices(s):
    start_idx = 6
    end_idx = 9
    substr = s[start_idx:end_idx + 1].lower()
    unique_substr_chars = set(substr)
    possible_perms = set(permutations(unique_substr_chars, len(unique_substr_chars)))
    palindromes = set()
    for perm in possible_perms:
        candidate_str = ''.join(perm)
        if candidate_str == candidate_str[::-1]:
            if len(candidate_str) >= 3:
                palindromes.add(candidate_str)
    return palindromes