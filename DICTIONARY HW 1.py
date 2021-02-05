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


##this function does literally nothing helpful!!!!##
def strip_string(file_contents):
    undesired = ["'", '"', ",", ".", "!", ":", ";", "#", "@", "?"]
    file_contents = file_contents.split()
    for ch in file_contents:
        if ch in undesired:
            file_contents = file_contents.remove[ch]
    return file_contents


def split_it_up(clean_string, text_dictionary):
    for word in clean_string:
        if word in text_dictionary:
            text_dictionary[word] += 1
        else:
            text_dictionary[word] = 1

    return text_dictionary


main()