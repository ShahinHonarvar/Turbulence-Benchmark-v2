def return_vowels(text):
    vowels = 'aeiou'
    result = []
    for i in range(19, 20):
        if text[i] in vowels and text[i] > '<' and (text[i] <= 'p'):
            result.append(text[i])
    return result