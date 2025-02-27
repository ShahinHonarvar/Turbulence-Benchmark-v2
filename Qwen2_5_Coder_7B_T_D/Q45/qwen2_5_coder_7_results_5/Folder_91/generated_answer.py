def palindromes_between_indices(s):
    s = s[2:7].lower()
    letters = set(s)
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            sub = ''.join(sorted(s[i:j]))
            if sub in letters and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes