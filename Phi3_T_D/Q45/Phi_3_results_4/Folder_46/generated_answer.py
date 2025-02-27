def is_palindrome(s):
    return s == s[::-1]

def get_all_permutations(chars):
    if len(chars) <= 1:
        return [chars]
    perms = []
    for i, char in enumerate(chars):
        without_char = chars[:i] + chars[i + 1:]
        for perm in get_all_permutations(without_char):
            perms.append([char] + perm)
    return perms

def palindromes_between_indices(s):
    char_set = set(s[4:10].lower())
    if len(char_set) < 6:
        return set()
    all_perms = get_all_permutations(list(char_set))
    palindromes = {tuple(''.join(perm)) for perm in all_perms if is_palindrome(''.join(perm))}
    return palindromes