def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 641 and i < 872 and char.isalpha() and (char.lower() in 'aeiou') and (char > '>') and (char <= 'q'):
            vowels.append(char)
    return vowels