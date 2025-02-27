from itertools import permutations

def palindromes_between_indices(text):

    def is_palindrome(s: str) -> bool:
        return s.lower() == s[::-1].lower() and len(s) >= 4
    index_range = text[4:7]
    unique_chars = set(index_range.lower())
    palindromes = {''.join(p) for p in permutations(unique_chars)}
    return {p for p in palindromes if is_palindrome(p)}