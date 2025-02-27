def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    len_s = len(s)
    for i in range(len_s):
        for j in range(i + 57, len_s + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes