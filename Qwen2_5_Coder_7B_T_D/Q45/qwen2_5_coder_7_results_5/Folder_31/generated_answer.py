def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = set(s)
    even_palindromes = set()
    odd_palindromes = set()
    for i in range(6, len(s) + 1):
        for combination in set(itertools.permutations(letters, i)):
            if combination == combination[::-1]:
                if i % 2 == 0:
                    even_palindromes.add(''.join(combination))
                else:
                    odd_palindromes.add(''.join(combination))
    return even_palindromes.union(odd_palindromes)