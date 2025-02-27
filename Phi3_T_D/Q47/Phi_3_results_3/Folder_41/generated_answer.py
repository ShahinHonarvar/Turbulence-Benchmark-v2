def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(1, 5):
        word = text[i:i + 3].lower()
        if is_palindrome(word.strip(string.punctuation + string.digits)):
            palindromes.add(word)
        word = text[i:i + 4].lower()
        if is_palindrome(word.strip(string.punctuation + string.digits)):
            palindromes.add(word)
    return palindromes