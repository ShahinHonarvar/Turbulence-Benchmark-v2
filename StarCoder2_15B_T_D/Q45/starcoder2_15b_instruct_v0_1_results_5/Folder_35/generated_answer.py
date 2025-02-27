def palindromes_between_indices(string):
    letters = sorted(set(string[2:5]))
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes