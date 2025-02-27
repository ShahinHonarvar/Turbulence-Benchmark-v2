def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = set(s)
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(3, len(letters) + 1):
        for combination in combinations(letters, length):
            for perm in permutations(combination):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word)
    return palindromes