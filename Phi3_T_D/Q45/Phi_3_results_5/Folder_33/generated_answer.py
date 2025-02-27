from itertools import permutations

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindromes_between_indices(s):
    substring = s[7:10].lower()
    letters = ''.join(sorted(set(substring.replace(' ', ''))))
    palindromes = set()
    length = min(4, len(letters))
    for perm in permutations(letters, length):
        palindrome_candidate = ''.join(perm) + ''.join(reversed(perm))
        if is_palindrome(palindrome_candidate):
            palindromes.add(palindrome_candidate)
    return palindromes