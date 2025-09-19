def get_num_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def get_num_letters(text):
    lower_text = text.lower()
    letter_dictionary = {}

    for letter in lower_text:
       if letter not in letter_dictionary:
           letter_dictionary[letter] = 1
       else:
           letter_dictionary[letter]+=1
    
    return letter_dictionary

def sort_on(dictionary):
    return dictionary["num"]


def sort_dictionary(dictionary):
    list_of_dicts =[]
    for item in dictionary:
        list_of_dicts.append({"char": item, "num": dictionary[item]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts


    