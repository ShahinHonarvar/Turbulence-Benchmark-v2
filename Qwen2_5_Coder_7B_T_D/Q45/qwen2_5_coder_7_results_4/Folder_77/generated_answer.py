def palindromes_between_indices(s):
    indices = s[4:7]
    letters = set(indices.lower())
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        palindrome = letters[i] + letters[j] + letters[k] + letters[l] + letters[m]
                        if palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
    return palindromes