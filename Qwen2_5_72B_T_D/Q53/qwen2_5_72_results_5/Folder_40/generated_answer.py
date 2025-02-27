def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    found_palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 2, length):
            if is_palindrome(s[i:j + 1]):
                found_palindromes.add(s[i:j + 1])
    return found_palindromes