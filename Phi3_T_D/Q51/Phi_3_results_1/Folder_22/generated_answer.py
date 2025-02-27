from collections import defaultdict

def if_contains_anagrams(str_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams_count = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3:
                if normalize(str_list[i]) == normalize(str_list[j]):
                    anagrams_count += 1
                    if anagrams_count > 14:
                        return False
    return True