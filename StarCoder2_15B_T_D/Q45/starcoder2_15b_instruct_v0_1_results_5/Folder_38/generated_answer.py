def palindromes_between_indices(string):
    chars = [char for char in string if char.isalpha()]
    palindromes = set()
    for i in range(3, 9):
        for j in range(i + 1, 9):
            for permutation in itertools.permutations(chars[i:j]):
                palindrome = ''.join(permutation)
                if palindrome.lower() == palindrome[::-1].lower():
                    palindromes.add(palindrome)
    return palindromes