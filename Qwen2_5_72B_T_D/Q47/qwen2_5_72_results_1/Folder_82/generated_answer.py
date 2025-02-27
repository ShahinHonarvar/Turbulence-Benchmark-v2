def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    s = s[3:301]
    result = set()
    for start in range(len(s)):
        for end in range(start + 30, min(len(s), start + 300) + 1):
            if is_palindrome(s[start:end]) and s[start:end].isalpha():
                result.add(s[start:end])
    return result