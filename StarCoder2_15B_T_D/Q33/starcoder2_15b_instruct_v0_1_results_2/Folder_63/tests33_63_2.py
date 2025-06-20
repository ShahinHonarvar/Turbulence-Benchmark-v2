from Q33.starcoder2_15b_instruct_v0_1_results_2.Folder_63.generated_answer import return_vowels
import string
import random


def test_repeat_consonant_char():
    s = 'm' * (69 + 2)
    assert not return_vowels(s)
   

def test_distinct_consonant_chars():
    s = 'BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy'
    assert not return_vowels(s)


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(69*100))
    assert len(return_vowels(s)) <= len(s)


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(69*2))
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    returned_s = return_vowels(s)
    sliced_s = s[34:69]
    for char in sliced_s:
        if char in vowels and '_' < char <= 'o':
            assert char in returned_s


def test_no_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(34)) + 'd' * (69-34) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))

    assert not return_vowels(s)


def test_all_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(34)) + 'i' * (69-34) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))
    
    if '_' < 'i' <= 'o':
        assert return_vowels(s) == ['i' for _ in range(69-34)]
    else:
        assert not return_vowels(s)
        