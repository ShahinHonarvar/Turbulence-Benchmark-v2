def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    sub_string = s[2:9]
    palindromes = set()
    for length in range(3, 5):
        for start in range(len(sub_string) - length + 1):
            candidate = sub_string[start:start + length]
            if is_palindrome(candidate) and candidate.isalpha():
                palindromes.add(candidate.lower())
    return palindromes