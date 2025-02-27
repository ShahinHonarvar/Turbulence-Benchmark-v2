def is_palindrome(s):
    return s == s[::-1]

def generate_permutations(chars):
    if len(chars) == 0:
        return ['']
    permutations = []
    for i in range(len(chars)):
        rest = chars[:i] + chars[i + 1:]
        for perm in generate_permutations(rest):
            permutations.append(chars[i] + perm)
    return permutations

def palindromes_between_indices(text):
    target_chars = ''.join((char.lower() for char in text[0:6] if char.isalpha()))
    perms = generate_permutations(target_chars)
    return {perm for perm in perms if len(perm) >= 6 and is_palindrome(perm)}