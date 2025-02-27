def palindromes_between_indices(string):
    filtered_chars = [char for char in string if 2 <= string.index(char) <= 6]
    permutations = set()

    def find_permutations(chars, permutation):
        if len(chars) == 0:
            permutations.add(''.join(permutation))
        else:
            for i in range(len(chars)):
                find_permutations(chars[:i] + chars[i + 1:], permutation + [chars[i]])
    find_permutations(filtered_chars, [])
    palindromes = set()
    for permutation in permutations:
        palindromes.add(permutation + ''.join(reversed(permutation)))
    palindromes = {palindrome for palindrome in palindromes if len(palindrome) >= 3}
    return set((palindrome.lower() for palindrome in palindromes))