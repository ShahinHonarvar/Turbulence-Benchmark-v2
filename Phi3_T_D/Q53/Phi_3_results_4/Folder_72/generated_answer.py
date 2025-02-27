def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 88, len(text) + 1):
            word = text[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes