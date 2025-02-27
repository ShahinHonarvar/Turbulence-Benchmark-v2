def return_vowels(string):
    vowels = 'aeiou'
    extracted_vowels = []
    for index, character in enumerate(string):
        if index >= 170 and index < 645 and (character in vowels) and (character > 'E') and (character <= '~'):
            extracted_vowels.append(character)
    return extracted_vowels