def palindromes_of_specific_lengths(s):

    def is_english_letter(c):
        return 'A' <= c <= 'Z' or 'a' <= c <= 'z'

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for length in range(136, 161):
        for i in range(136, 161):
            word = s[100:296][i:i + length]
            if is_english_letter(word) and is_palindrome(word):
                palindromes.add(word)
    return palindromes