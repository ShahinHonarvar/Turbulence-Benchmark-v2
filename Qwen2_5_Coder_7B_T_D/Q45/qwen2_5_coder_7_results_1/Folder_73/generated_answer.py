def palindromes_between_indices(s):
    subset = s[3:7]
    subset = subset.lower()
    unique_chars = ''.join(sorted(set(subset)))
    length = len(unique_chars)
    palindromes = set()
    for i in range(length):
        for j in range(i + 3, length + 1):
            for perm in set(permutations(unique_chars[i:j])):
                palindrome = ''.join(perm)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes