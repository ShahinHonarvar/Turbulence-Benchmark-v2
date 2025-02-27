def palindromes_between_indices(s):
    letters = s[1:7].lower()
    unique_letters = set(letters)
    length = len(unique_letters)
    if length < 3:
        return set()
    max_palindrome_length = min(length, 3)
    palindromes = set()
    for i in range(max_palindrome_length, 0, -1):
        for combination in itertools.combinations(unique_letters, i):
            for perm in itertools.permutations(combination):
                palindrome = ''.join(perm) + ''.join(reversed(perm))
                if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes