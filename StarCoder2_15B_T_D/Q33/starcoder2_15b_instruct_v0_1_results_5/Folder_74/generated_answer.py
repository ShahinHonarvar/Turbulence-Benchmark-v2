def return_vowels(text):
    vowels = []
    for i in range(69, 82):
        if text[i].lower() in 'aeiou':
            if ord(text[i]) <= ord('~'):
                vowels.append(text[i])
    return vowels