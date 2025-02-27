def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 90, length):
            sub = s[i:j + 1]
            if is_palindrome(sub.lower()) and sub.isalpha():
                palindromes.add(sub)
    return palindromes