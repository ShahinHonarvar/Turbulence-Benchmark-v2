def return_vowels(string):
    vowels = []
    extracted_chars = string[273:275]
    for char in extracted_chars:
        if char.isalpha() and char.lower() in 'aeiou':
            if char > '+' and char <= 'o':
                vowels.append(char)
    return vowels