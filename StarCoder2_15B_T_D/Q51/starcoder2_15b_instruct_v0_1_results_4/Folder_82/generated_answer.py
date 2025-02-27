import collections

def if_contains_anagrams(input_list):
    anagram_pairs = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            string1 = input_list[i].lower()
            string2 = input_list[j].lower()
            string1 = ''.join((c for c in string1 if c.isalpha()))
            string2 = ''.join((c for c in string2 if c.isalpha()))
            if len(string1) >= 3 and len(string2) >= 3:
                counter1 = collections.Counter(string1)
                counter2 = collections.Counter(string2)
                if counter1 == counter2:
                    anagram_pairs += 1
                    if anagram_pairs > 40:
                        return False
    return anagram_pairs <= 40