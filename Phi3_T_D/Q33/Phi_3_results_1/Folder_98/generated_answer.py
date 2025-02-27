def return_vowels(input_string):
    vowels_list = []
    vowels = 'AEIOUaeiou'
    for i in range(3, 9):
        if input_string[i] in vowels and ord('a') <= ord(input_string[i]) <= ord('u'):
            vowels_list.append(input_string[i])
    return vowels_list