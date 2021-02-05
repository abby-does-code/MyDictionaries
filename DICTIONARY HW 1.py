# START#
# This program turns a text into a dict#

undesired = ["'", '"', ",", ".", "!", ":", ";", "#", "@", "?"]


def main():
    text_dictionary = {}
    infile = open("text.txt", "r")
    file_contents = infile.read()
    clean_string = strip_punct(file_contents, undesired)
    text_dictionary = split_it_up(clean_string, text_dictionary)

    for word, count in sorted(text_dictionary.items()):
        print(word, count)


def strip_punct(file_contents, undesired):

    strg_to_check = str(file_contents.upper())

    for ch in undesired:
        strg_to_check = strg_to_check.replace(ch, "")

    print(strg_to_check)
    return strg_to_check


def split_it_up(clean_string, text_dictionary):
    clean_string = clean_string.split()
    for word in clean_string:
        if word in text_dictionary:
            text_dictionary[word] += 1
        else:
            text_dictionary[word] = 1

    return text_dictionary


main()