def return_vowels(string: str) -> list:
    vowels = []
    for i, char in enumerate(string):
        if char in 'aeiou':
            if 10 <= i < 83 and char > '%' and (char <= 'e'):
                vowels.append(char)
    return vowels