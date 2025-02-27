def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(n):
        for j in range(i + 25, n + 1):
            if is_palindrome(s[i:j]):
                if s[i:j].isalpha():
                    palindromes.add(s[i:j])
    return palindromes