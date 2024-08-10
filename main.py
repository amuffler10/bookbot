def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    #text of book 
    
    book_words = text.split()
    count = count_words(book_words)
    #print(count)
    #count of words

    lowercase_words = text.lower()
    alphabet_count = count_characters(lowercase_words)
    #print(alphabet_count)
    #dictionary of letter, count 

    dic_list_alpha_count = convert_dict_to_dict_list(alphabet_count)
    dic_list_alpha_count.sort(reverse=True, key=sort_on)
    #print(dic_list_alpha_count)
    #converts dictionary of letter, count to list of dictionarys

    make_report(book_path,count,dic_list_alpha_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(words):
    count = 0
    for word in words:
        count +=1
    return count

def count_characters(words):
    alphabet_dict = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "o" : 0,
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0
    }
    for char in words:
        if char in alphabet_dict:
            alphabet_dict[char] += 1
    return alphabet_dict

def convert_dict_to_dict_list(dict):
    dict_list = []
    for key in dict:
        dict_list.append({"name": key , "num": dict[key]})
    return dict_list

def sort_on(dict):
    return dict["num"]

def make_report(path, count, list_of_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the document")
    print()
    for d in list_of_dict:
        char = d["name"]
        char_count = d["num"]
        print(f"The '{char}' character was found {char_count} times")
    print(f"--- End report ---")

main()