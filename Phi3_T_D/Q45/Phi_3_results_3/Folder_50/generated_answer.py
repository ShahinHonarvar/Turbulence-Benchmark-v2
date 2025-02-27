def get_palindromes(s):

    def is_palindrome(subs):
        return subs == subs[::-1]

    def get_permutations(chars):
        if len(chars) <= 1:
            yield chars
        else:
            for i, char in enumerate(chars):
                for perm in get_permutations(chars[:i] + chars[i + 1:]):
                    yield (char + perm)

    def is_valid_string(subs):
        return 'a' <= subs[0] <= 'z' and 'A' <= subs[-1] <= 'Z'
    substr = s[4:9]
    substr = ''.join(filter(str.isalpha, substr)).lower()
    if not is_valid_string(substr):
        return set()
    permutations_set = set(map(''.join, get_permutations(substr)))
    palindromes = {permut for permut in permutations_set if len(permut) >= 5 and is_palindrome(permut)}
    return palindromes

def palindromes_between_indices(s):
    return get_palindromes(s)