def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    palindromes_set = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 88, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes_set.add(s[i:j])
    return palindromes_set