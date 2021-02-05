# START#
# This program turns a text into a dict#


def main():
    text_dictionary = {}

    infile = open("text.txt", "r")
    file_contents = infile.read()
    clean_string = strip_string(file_contents)
    text_dictionary = split_it_up(clean_string, text_dictionary)

    # print(f'{"WORD":<12}COUNT')

    for word, count in sorted(text_dictionary.items()):
        print(word, count)


def strip_string(file_contents):
    undesired = ["'", '"', ",", ".", "!", ":", ";", "#", "@", "?"]
    str_check = file_contents.upper()
    for x in undesired:
        clean_string = str_check.replace(x, " ")
    print(clean_string)
    return clean_string


def split_it_up(clean_string, text_dictionary):
    for word in clean_string.split():
        if word in text_dictionary:
            text_dictionary[word] += 1
        else:
            text_dictionary[word] = 1

    return text_dictionary


main()