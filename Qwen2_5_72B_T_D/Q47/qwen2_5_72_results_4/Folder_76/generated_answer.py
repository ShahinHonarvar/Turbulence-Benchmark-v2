def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    sub_str = s[101:293]
    palindromes = set()
    for start in range(len(sub_str)):
        for end in range(start + 154, min(start + 183, len(sub_str) + 1)):
            candidate = sub_str[start:end]
            if is_palindrome(candidate) and candidate.isalpha():
                palindromes.add(candidate.lower())
    return palindromes