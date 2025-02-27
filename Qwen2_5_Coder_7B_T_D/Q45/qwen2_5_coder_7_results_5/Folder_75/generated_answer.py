def palindromes_between_indices(s):
    letters = s[2:5]
    letters = letters.lower()
    unique_letters = set(letters)
    palindromes = set()
    for length in range(3, 6):
        for i in range(len(letters) - length + 1):
            for perm in set(permutations(letters[i:i + length])):
                palindrome = ''.join(perm)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes