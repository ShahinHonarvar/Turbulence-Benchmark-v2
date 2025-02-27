def palindromes_between_indices(s):
    s = s[:9].lower()
    letters = sorted(s)
    n = len(s)
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(n):
        for j in range(i + 6, n + 1):
            for perm in set(itertools.permutations(letters[i:j])):
                sub = ''.join(perm)
                if is_palindrome(sub):
                    palindromes.add(sub)
    return palindromes