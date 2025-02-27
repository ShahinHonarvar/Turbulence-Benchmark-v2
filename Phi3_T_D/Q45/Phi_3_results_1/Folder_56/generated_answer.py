from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    middle_slice = s[5:10]
    chars = [char for char in middle_slice.lower() if char.isalpha()]
    if len(chars) < 5:
        return set()
    palindrome_set = set()
    for perm_len in range(5, len(chars) + 1):
        for perm in permutations(chars, perm_len):
            for i in range(len(perm) // 2 + 1):
                left, right = (perm[:i], perm[i:])
                if is_palindrome(''.join(left) + ''.join(right[::-1])):
                    palindrome_set.add(''.join(perm).capitalize())
    return palindrome_set