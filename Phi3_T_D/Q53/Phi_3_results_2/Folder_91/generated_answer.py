def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 7, len(s) + 1):
            sub_str = s[i:j].lower()
            if is_palindrome(sub_str):
                palindromes.add(sub_str)
    return palindromes