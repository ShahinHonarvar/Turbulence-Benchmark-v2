def palindromes_between_indices(s):
    letters = s[2:8].lower()
    distinct_letters = set(letters)
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for length in range(6, len(distinct_letters) + 1):
        for combination in combinations(distinct_letters, length):
            for perm in permutations(combination):
                candidate = ''.join(perm)
                if is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes