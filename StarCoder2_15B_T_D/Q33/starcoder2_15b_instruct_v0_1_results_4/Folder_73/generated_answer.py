def return_vowels(input_str):
    vowels = []
    for i, c in enumerate(input_str):
        if 47 <= i < 89 and c.isalpha() and (c.lower() in 'aeiou') and (c > '@') and (c <= 'n'):
            vowels.append(c)
    return vowels