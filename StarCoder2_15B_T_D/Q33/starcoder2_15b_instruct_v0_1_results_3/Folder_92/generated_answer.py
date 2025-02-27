def return_vowels(string):
    vowels = []
    for char in string[3:8]:
        if char.isalpha() and char.lower() in 'aeiou' and (';' < char <= 'D'):
            vowels.append(char)
    return vowels