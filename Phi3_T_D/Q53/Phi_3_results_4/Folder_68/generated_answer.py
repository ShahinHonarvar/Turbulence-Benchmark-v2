def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    found_palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 20, len(s) + 1):
            word = s[i:j]
            if word.isalpha() and is_palindrome(word):
                found_palindromes.add(word)
    return found_palindromes