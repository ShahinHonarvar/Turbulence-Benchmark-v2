def palindromes_between_indices(s):
    range_chars = s[3:7].lower()
    unique_chars = set(range_chars)
    palindromes = set()
    for length in range(4, len(unique_chars) + 1):
        for chars in itertools.permutations(unique_chars, length):
            for perm in set(itertools.permutations(chars)):
                palindrome = ''.join(perm)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes