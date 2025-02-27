def return_vowels(string):
    vowels = 'aeiou'
    vowels_list = []
    for i in range(23, 85):
        if i < len(string) and string[i] in vowels and (string[i] > 'W') and (string[i] <= 'v'):
            vowels_list.append(string[i])
    return vowels_list