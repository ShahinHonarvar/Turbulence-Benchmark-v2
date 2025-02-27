def return_vowels(string):
    vowels = [char for char in string if char.isalpha() and char.lower() in 'aeiou']
    result = []
    for i, char in enumerate(string):
        if i >= 59 and i < 61 and char.isalpha() and (char.lower() in vowels) and (char > '+') and (char <= 'h'):
            result.append(char)
    return result