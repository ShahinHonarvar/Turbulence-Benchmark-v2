def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    s = s[1:300]
    found_palindromes = set()
    for length in range(3, 11):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                found_palindromes.add(substring.lower())
    return found_palindromes