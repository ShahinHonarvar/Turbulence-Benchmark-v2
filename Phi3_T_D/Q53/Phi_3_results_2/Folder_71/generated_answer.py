def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 87, length + 1):
            potential_palindrome = s[i:j]
            if is_palindrome(potential_palindrome):
                palindromes.add(potential_palindrome.lower())
    return palindromes