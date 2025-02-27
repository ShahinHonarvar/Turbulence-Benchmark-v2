def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    n = len(s)
    found_palindromes = set()
    for i in range(n):
        for j in range(i + 22, n):
            candidate = s[i:j + 1]
            if is_palindrome(candidate):
                found_palindromes.add(candidate)
    return found_palindromes