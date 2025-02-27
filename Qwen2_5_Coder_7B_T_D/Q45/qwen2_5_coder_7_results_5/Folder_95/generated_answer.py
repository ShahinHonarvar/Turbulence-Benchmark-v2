def palindromes_between_indices(s):
    letters = set(s[7:9].lower())
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            palindrome = ''.join(sorted(letters[i:j] + letters[k:l] + letters[m:n]))
                            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                                palindromes.add(palindrome)
    return palindromes