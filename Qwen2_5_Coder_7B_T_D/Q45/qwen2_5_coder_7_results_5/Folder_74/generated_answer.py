import itertools

def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = set(s)
    palindromes = set()
    for r in range(3, 7):
        for combo in itertools.combinations_with_replacement(letters, r):
            perm = ''.join(combo)
            for p in set(itertools.permutations(perm)):
                palindrome = ''.join(p)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes