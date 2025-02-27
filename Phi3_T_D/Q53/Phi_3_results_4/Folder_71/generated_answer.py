def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_english_letters(word):
        return all(('a' <= c <= 'z' for c in word))
    palindromes = set()
    s = s.lower()
    n = 87
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            word = s[i:j]
            if is_english_letters(word) and is_palindrome(word):
                palindromes.add(word)
    return palindromes