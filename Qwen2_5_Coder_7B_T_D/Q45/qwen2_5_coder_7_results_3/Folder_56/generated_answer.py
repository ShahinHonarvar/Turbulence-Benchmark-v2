def palindromes_between_indices(s):
    letters = set(s[5:10].lower())
    if len(letters) < 5:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for m in range(l + 1, len(letters)):
                        palindrome = ''.join(sorted(letters))[:m + 1] + ''.join(sorted(letters))[:m + 1][::-1]
                        if len(palindrome) >= 5:
                            palindromes.add(palindrome)
    return palindromes