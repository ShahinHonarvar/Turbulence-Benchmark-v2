def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    n = 86
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                clean_sub = ''.join(filter(str.isalpha, sub)).lower()
                if len(clean_sub) >= n:
                    palindromes.add(clean_sub)
    return palindromes