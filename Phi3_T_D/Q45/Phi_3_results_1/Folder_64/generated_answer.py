def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(text):
    return set(filter(is_palindrome, (''.join(perm) for perm in itertools.permutations(text[3:10].lower()) if len(perm) >= 5)))