from itertools import combinations, permutations

def is_palindrome(s):
    return s.lower() == s[::-1].lower() and len(s) >= 4

def actual_palindromes(chars, length):
    palindromes_set = set()
    if length < 4:
        for combo in combinations(chars, length):
            permuted_combinations = set(permutations(combo))
            for permuted in permuted_combinations:
                palindrome = ''.join(permuted)
                if is_palindrome(palindrome):
                    palindromes_set.add(palindrome)
    else:
        all_permutations = set(permutations(chars, length))
        for permuted in all_permutations:
            palindrome = ''.join(permuted)
            if is_palindrome(palindrome):
                palindromes_set.add(palindrome)
    return palindromes_set

def palindromes_between_indices(s):
    subset = s[2:6].lower()
    palindrome_set = actual_palindromes(subset, 4)
    return palindrome_set