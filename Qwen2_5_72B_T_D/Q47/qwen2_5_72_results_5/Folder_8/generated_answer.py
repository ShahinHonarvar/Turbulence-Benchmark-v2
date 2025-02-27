def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    if len(s) < 73:
        return set()
    substring = s[17:73]
    palindromes = set()
    for length in range(50, 52):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment.isalpha() and is_palindrome(segment):
                palindromes.add(segment)
    return palindromes