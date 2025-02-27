from itertools import permutations

def palindromes_between_indices(s):

    def generate_palindromes(chars):
        pals = set()
        for perm in permutations(chars, 2):
            perm_str = ''.join(perm)
            if len(perm_str) >= 2:
                for middle in chars:
                    palindrome = perm_str[0] + middle + perm_str[1]
                    if palindrome.lower() == palindrome[::-1].lower():
                        pals.add(palindrome)
        return pals
    chars = s[3:5]
    if not chars.isalpha():
        return set()
    return generate_palindromes(chars.lower())