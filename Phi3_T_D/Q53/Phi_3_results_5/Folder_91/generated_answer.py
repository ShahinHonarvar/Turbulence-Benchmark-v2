def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(len(s) - 6):
        for j in range(i + 7, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes