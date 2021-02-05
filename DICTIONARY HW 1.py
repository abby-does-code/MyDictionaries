# START#
# This program turns a text into a dict#


def main():
    text_dictionary = {}

    infile = open("text.txt", "r")
    file_contents = infile.read()
    clean_string = strip_string(file_contents)
    text_dictionary = split_it_up(clean_string, text_dictionary)

    for word, count in sorted(text_dictionary.items()):
        print(word, count)


##this function does literally nothing helpful!!!!##
def strip_string(file_contents):
    undesired = ["'", '"', ",", ".", "!", ":", ";", "#", "@", "?"]
    for ch in undesired:
        clean_string = file_contents.rstrip(ch)
    return clean_string


def split_it_up(clean_string, text_dictionary):
    clean_string = clean_string.split()
    for word in clean_string:
        if word in text_dictionary:
            text_dictionary[word] += 1
        else:
            text_dictionary[word] = 1

    return text_dictionary


main()