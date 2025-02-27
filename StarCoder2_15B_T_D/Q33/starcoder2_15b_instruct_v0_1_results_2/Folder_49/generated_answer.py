def return_vowels(string):
    vowels_list = []
    for i in range(10, 97):
        char = string[i]
        if char.isalpha() and char.islower() and (char > 'r') and (char <= 'b'):
            vowels_list.append(char)
    return vowels_list