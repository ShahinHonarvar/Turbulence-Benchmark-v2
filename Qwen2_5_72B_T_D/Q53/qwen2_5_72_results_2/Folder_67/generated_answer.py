def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    length = len(s)
    s = s.lower()
    found_palindromes = set()
    for start in range(length):
        for end in range(start + 25, length + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes