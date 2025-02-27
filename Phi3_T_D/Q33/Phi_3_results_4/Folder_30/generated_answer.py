def return_vowels(text):
    result = []
    for char in text[11:61]:
        if 'M' < char <= 'W' and char in 'aeiouAEIOU':
            result.append(char)
    return result