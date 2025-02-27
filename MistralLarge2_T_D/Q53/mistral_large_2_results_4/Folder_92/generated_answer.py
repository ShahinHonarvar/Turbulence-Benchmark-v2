def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    n = 10
    cleaned_s = ''.join(filter(str.isalpha, s)).lower()
    length = len(cleaned_s)
    palindromes = set()
    for i in range(length):
        for j in range(i + n, length + 1):
            sub = cleaned_s[i:j]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes