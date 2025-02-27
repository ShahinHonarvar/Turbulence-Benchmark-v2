def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[:6].lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    results = []
    for length in range(3, 6):
        for i in range(len(substring) - length + 1):
            if all((char in alphabet for char in substring[i:i + length])):
                if is_palindrome(substring[i:i + length]):
                    results.append(substring[i:i + length])
    return set(results)