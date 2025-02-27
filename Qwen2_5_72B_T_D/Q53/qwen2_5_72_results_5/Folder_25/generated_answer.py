def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def is_palindrome(sub):
        return sub == sub[::-1]
    found_palindromes = set()
    for i in range(len(s)):
        for j in range(i + 37, len(s) + 1):
            if is_palindrome(s[i:j]):
                found_palindromes.add(s[i:j])
    return found_palindromes