def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1] and all(('a' <= char.lower() <= 'z' for char in word))
    result_set = set()
    for length in range(3, 61):
        start, end = (70, min(140, len(s)))
        for i in range(start, end - length + 2):
            substring = s[i:i + length]
            if is_palindrome(substring):
                result_set.add(substring.upper())
    return result_set