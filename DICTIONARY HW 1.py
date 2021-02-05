# START#
# This program turns a text into a dict#

text_dictionary = {}


def main():
    infile = open("text.txt", "r")
    file_contents = str(infile.read())
    split_it_up(file_contents)

    print(f'{"WORD":<12}COUNT')


def split_it_up(file_contents):
    for word in file_contents.split():

        if word in text_dictionary:
            text_dictionary[word] += 1
    else:
        text_dictionary[word] = 1

    return text_dictionary


main()