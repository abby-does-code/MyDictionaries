number_of_wins = {}


def main():
    infile = open("worldserieswinners.txt", "r")
    team_num_wins(infile)


def team_num_wins(infile):

    winners_txt = infile.readlines()
    for line in winners_txt:
        if line in number_of_wins:
            number_of_wins[line] += 1
        else:
            number_of_wins[line] = 1
    print(number_of_wins, end="")


def assign_years(infile):
    line_number = 1903
    for line in infile.readlines():
        line_number += 1


main()