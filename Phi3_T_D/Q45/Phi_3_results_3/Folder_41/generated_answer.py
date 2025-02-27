from itertools import permutations

def palindromes_between_indices(s):
    start, end = (2, 3)
    filtered_chars = [ch for ch in s[start:end] if ch.isalpha()]
    if len(filtered_chars) < 3:
        return set()
    palindromes = set()
    for perm in permutations(filtered_chars):
        palindrome = ''.join(perm) + ''.join(reversed(perm))
        if palindrome.lower() == palindrome[::-1].lower():
            palindromes.add(palindrome)
    return palindromes