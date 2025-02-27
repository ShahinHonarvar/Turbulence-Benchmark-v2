def return_vowels(s):
    vowels = []
    for i in range(65, 70):
        char = chr(i)
        if char > '%' and char <= 'G':
            vowels.append(char)
    return vowels