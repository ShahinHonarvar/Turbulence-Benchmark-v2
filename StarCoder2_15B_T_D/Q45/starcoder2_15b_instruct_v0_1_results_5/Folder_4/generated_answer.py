def palindromes_between_indices(string):
    chars = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for i in range(3, 10):
        for j in range(i + 1, 10):
            for permutation in itertools.permutations(chars[i:j]):
                palindrome = ''.join(permutation)
                if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes