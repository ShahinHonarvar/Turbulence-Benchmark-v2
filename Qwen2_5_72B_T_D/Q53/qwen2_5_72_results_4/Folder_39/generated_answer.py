def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def is_palindrome(sub):
        return sub == sub[::-1]
    found_palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 68, n):
            if is_palindrome(s[i:j + 1]):
                found_palindromes.add(s[i:j + 1])
    return found_palindromes