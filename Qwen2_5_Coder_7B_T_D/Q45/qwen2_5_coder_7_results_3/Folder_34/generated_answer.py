def palindromes_between_indices(s):
    letters = s[5:8].lower()
    if len(letters) < 3:
        return set()
    letters = ''.join(sorted(set(letters)))
    length = len(letters)

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(length):
        for j in range(i + 3, length + 1):
            for k in range(j + 3, length + 1):
                comb = ''.join(letters[i:j + k - i])
                if is_palindrome(comb):
                    palindromes.add(comb)
    return palindromes