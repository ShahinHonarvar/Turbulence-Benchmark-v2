from itertools import permutations

def is_palindrome(seq):
    return seq == seq[::-1]

def generate_palindromes(subset):
    subset_len = len(subset)
    if subset_len < 5:
        return set()
    half_len = subset_len // 2
    for i in range(half_len + 1):
        prefix_permutations = set(permutations(subset[:i]))
        for perm in prefix_permutations:
            reversed_prefix = perm[::-1]
            remaining_chars = ''.join(subset[i:half_len])
            palindrome_half = ''.join(perm) + remaining_chars[half_len:]
            palindrome_candidate = palindrome_half.lower() + reversed_prefix
            if is_palindrome(palindrome_candidate):
                yield palindrome_candidate

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    word_subset = s[4:8].lower()
    return set(generate_palindromes(word_subset))