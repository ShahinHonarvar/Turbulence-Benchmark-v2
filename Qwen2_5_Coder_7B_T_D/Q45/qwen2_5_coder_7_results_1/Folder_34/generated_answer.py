def palindromes_between_indices(s):
    letters = s[5:8].lower()
    letters_set = set(letters)
    length = len(letters_set)
    if length < 2:
        return set()
    palindromes = set()
    for i in range(length):
        for j in range(i, length):
            for k in range(i, length):
                for l in range(k, length):
                    for m in range(l, length):
                        palindrome = letters_set[i] + letters_set[j] + letters_set[k] + letters_set[l] + letters_set[m]
                        if palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
    return palindromes