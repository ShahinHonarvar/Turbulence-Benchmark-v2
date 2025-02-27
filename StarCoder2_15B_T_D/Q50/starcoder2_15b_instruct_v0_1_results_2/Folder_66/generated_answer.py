import itertools

def if_contains_anagrams(input_list):
    anagrams = []
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if sorted(input_list[i].lower()) == sorted(input_list[j].lower()) and len(input_list[i]) >= 3:
                anagrams.append((input_list[i], input_list[j]))
    return len(anagrams) >= 92