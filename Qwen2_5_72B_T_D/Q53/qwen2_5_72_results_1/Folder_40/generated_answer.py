def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def is_palindrome(sub):
        return sub == sub[::-1]
    found_palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 3, n + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                found_palindromes.add(sub)
    return found_palindromes