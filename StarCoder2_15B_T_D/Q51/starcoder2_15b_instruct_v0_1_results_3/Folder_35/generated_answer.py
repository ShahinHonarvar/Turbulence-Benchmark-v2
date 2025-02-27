def if_contains_anagrams(input_list):
    counter = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            first_string = input_list[i]
            second_string = input_list[j]
            if len(first_string) >= 3 and len(second_string) >= 3:
                first_string = ''.join((c for c in first_string if c.isalpha())).lower()
                second_string = ''.join((c for c in second_string if c.isalpha())).lower()
                if sorted(first_string) == sorted(second_string):
                    counter += 1
                    if counter > 210:
                        return False
    return True