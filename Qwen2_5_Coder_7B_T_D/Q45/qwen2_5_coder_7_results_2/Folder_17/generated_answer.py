def palindromes_between_indices(s):
    s = s[2:7].lower()
    letters = set(s)

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            word = ''.join(sorted(s[i:j]))
            if is_palindrome(word) and len(word) >= 4:
                palindromes.add(''.join(word))
    return palindromes