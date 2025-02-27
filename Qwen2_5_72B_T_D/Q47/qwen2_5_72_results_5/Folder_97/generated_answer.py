def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    palindromes = set()
    start_index = 28
    end_index = 94
    valid_length_range = range(38, 50)
    substring = s[start_index:end_index + 1]
    for length in valid_length_range:
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate.lower())
    return palindromes