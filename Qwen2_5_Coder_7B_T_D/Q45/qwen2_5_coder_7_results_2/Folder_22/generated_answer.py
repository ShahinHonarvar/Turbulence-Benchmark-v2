def palindromes_between_indices(s):
    indices = set((s[i] for i in range(5, 7)))
    if len(indices) < 3:
        return set()
    letters = ''.join(sorted(indices))
    length = len(letters)
    palindromes = set()
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                for l in range(k + 1, length):
                    for m in range(l + 1, length):
                        for n in range(m + 1, length):
                            palindrome = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n]
                            if palindrome == palindrome[::-1]:
                                palindromes.add(palindrome)
    return palindromes