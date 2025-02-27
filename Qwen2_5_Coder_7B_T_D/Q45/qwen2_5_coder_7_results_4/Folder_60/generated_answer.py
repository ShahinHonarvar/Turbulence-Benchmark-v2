def palindromes_between_indices(s):
    letters = s[3:7]
    letters = letters.lower()
    unique_letters = set(letters)
    n = len(unique_letters)
    if n < 2:
        return set()
    palindromes = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(i + 1, n):
                for l in range(j + 1, n):
                    for m in range(k + 1, n):
                        palindrome = letters[i] + letters[j] + letters[k] + letters[l] + letters[m]
                        if palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
    return palindromes