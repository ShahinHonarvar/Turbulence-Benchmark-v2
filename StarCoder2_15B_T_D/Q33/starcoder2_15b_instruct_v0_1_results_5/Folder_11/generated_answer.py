def return_vowels(string):
    vowels = []
    for i in range(29, 73):
        if string[i] in 'aeiou' and string[i] > '#' and (string[i] <= '('):
            vowels.append(string[i])
    return vowels