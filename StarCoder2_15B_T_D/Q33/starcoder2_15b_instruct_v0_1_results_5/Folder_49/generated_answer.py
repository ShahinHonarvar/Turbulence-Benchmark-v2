def return_vowels(string: str) -> list:
    vowels = []
    for index, char in enumerate(string):
        if index >= 10 and index < 97:
            if char in 'AEIOU' and char > 'R' and (char <= 'b'):
                vowels.append(char)
    return vowels