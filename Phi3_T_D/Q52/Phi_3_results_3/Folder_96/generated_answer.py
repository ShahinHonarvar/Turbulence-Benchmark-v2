def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 82):
        substring = text[i:i + 83]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result