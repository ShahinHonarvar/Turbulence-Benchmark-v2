def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[11:84]
    s_filtered = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    for length in range(13, 67):
        for i in range(len(s_filtered) - length + 1):
            substring = s_filtered[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes