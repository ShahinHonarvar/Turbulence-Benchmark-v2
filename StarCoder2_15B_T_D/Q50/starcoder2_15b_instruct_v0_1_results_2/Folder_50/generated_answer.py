import collections

def if_contains_anagrams(input_list):
    count = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if len(input_list[i]) >= 3 and len(input_list[j]) >= 3 and (sorted(input_list[i].lower()) == sorted(input_list[j].lower())):
                count += 1
    return count >= 20