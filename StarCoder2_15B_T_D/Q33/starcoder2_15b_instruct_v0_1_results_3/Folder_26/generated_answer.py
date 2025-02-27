def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    matching_characters = []
    for i, character in enumerate(string):
        if i >= 10 and i < 82 and (character > '$') and (character <= '@'):
            if character in vowels:
                matching_characters.append(character)
    return matching_characters