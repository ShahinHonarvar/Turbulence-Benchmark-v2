def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]

    def is_alpha(word):
        return all((c.isalpha() for c in word))
    s = s[23:95]
    result = set()
    for length in range(17, 56):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring) and is_alpha(substring):
                result.add(substring)
    return result