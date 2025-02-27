def palindromes_between_indices(string):
    letters = [ch for ch in string if ch.isalpha()]
    palindromes = set()
    for i in range(4, 10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                palindrome = ''.join([letters[i], letters[j], letters[k]])
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes