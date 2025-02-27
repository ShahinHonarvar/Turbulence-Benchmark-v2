def return_vowels(string):
    vowels = []
    for i in range(10, 82):
        char = string[i]
        if char.isalpha() and char.lower() in 'aeiou':
            if char > '$' and char <= '@':
                vowels.append(char)
    return vowels