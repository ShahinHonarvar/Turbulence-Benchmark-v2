from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    s = s[0:7]
    targets = [char.lower() for char in s if char.isalpha()]
    unique_targets = set(targets)
    palindromes = set()
    for i in range(3, len(targets) + 1):
        for combo in permutations(unique_targets, i):
            combo_str = ''.join(combo)
            if is_palindrome(combo_str):
                palindromes.add(combo_str)
    return palindromes