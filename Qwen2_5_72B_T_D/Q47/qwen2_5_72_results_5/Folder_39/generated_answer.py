def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    sub_string = s[31:92]
    palindromes = set()
    for length in range(50, 54):
        for start in range(len(sub_string) - length + 1):
            substring = sub_string[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes