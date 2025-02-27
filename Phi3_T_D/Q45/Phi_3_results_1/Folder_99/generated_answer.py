from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    substring = s[4:9]
    unique_chars = set(substring.lower())
    palindromes = {''}
    for l in range(3, len(unique_chars) + 1):
        for perm in permutations(unique_chars, l):
            for i in range(len(perm)):
                c = perm[i]
                sub_perm = perm[:i] + perm[i + 1:]
                palindrome_candidate = c + ''.join(sub_perm) + c
                if is_palindrome(palindrome_candidate):
                    palindromes.add(palindrome_candidate)
    return palindromes