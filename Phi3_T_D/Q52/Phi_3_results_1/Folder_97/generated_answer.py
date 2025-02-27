def palindrome_of_length_n(text):
    result = set()
    text = text.lower()
    n = 210
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if subset and subset == subset[::-1]:
            result.add(substring)
    return result