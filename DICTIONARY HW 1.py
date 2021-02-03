# START#
# This program turns a text into a dict#

text_dictionary = {}


def main():
    infile = open("text.txt", "r")
    file_contents = infile.read()

    print(file_contents)
    split_it_up(file_contents)


main()


def split_it_up(file_contents):
    for x in file_contents:
        file_contents.split()
