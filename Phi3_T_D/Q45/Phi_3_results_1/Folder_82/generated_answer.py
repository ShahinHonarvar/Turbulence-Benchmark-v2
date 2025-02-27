from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    alpha_chars = [char.lower() for char in s[1:7]]
    unique_chars = set(alpha_chars)
    palindromes = set()
    for perm in permutations(unique_chars):
        merged = ''.join(perm)
        if len(merged) >= 7:
            center = merged[len(merged) // 2] if len(merged) % 2 == 1 else ''
            palindrome = merged[:len(merged) // 2] + center + merged[len(merged) // 2:][::-1]
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes