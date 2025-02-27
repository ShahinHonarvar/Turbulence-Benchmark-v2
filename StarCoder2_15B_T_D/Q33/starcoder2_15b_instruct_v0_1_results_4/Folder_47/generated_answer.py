def return_vowels(text):
    vowels = list('aeiou')
    result = []
    for char in text[23:38]:
        if char in vowels and char > 'N' and (char <= 'k'):
            result.append(char)
    return result