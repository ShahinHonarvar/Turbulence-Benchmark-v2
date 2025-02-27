def palindromes_between_indices(s):
    s = s[3:9].lower()
    characters = set(s)
    palindromes = set()
    for length in range(4, len(characters) + 1):
        for chars in itertools.permutations(characters, length):
            half_length = length // 2
            half = ''.join(chars[:half_length])
            if length % 2 == 0:
                palindrome = half + half[::-1]
            else:
                palindrome = half + chars[half_length] + half[::-1]
            palindromes.add(palindrome)
    return palindromes