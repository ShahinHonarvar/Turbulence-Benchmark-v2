def palindrome_of_length_n(text):
    text = text.lower()
    n = 78
    length = len(text)
    result = set()
    for i in range(length - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result