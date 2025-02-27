def palindrome_of_length_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    s = s.lower()
    half_length = (113 - 1) // 2
    for i in range(len(s) - 112):
        potential_palindrome = s[i:i + 113]
        if potential_palindrome.isalpha() and is_palindrome(potential_palindrome):
            palindromes.add(potential_palindrome.capitalize())
    return palindromes