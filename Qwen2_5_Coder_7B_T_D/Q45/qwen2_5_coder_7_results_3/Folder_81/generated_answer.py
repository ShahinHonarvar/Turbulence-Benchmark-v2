def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = set(s)

    def is_palindrome(word):
        return word == word[::-1]

    def get_permutations(letters, length):
        if length == 1:
            return set(letters)
        perms = set()
        for letter in letters:
            perms.update((letter + p for p in get_permutations(letters - {letter}, length - 1)))
        return perms
    palindromes = set()
    for length in range(3, len(s) + 1):
        perms = get_permutations(letters, length)
        palindromes.update((p for p in perms if is_palindrome(p)))
    return palindromes