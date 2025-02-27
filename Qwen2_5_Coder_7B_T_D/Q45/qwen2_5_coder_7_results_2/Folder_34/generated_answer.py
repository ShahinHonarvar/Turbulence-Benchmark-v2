def palindromes_between_indices(s):
    letters = s[5:8].lower()
    unique_letters = set(letters)
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i + 3, len(unique_letters) + 1):
            for perm in set(permutations(unique_letters[i:j])):
                palindrome = ''.join(perm) + ''.join(perm[-2::-1])
                palindromes.add(palindrome)
    return palindromes