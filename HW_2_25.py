number_of_wins = {}


def main():
    infile = open("worldserieswinners.txt", "r")

    team_num_wins(infile)


def team_num_wins(infile):
    winners_txt = str(infile.read())
    line = winners_txt.splitlines()
    for line in winners_txt:
        if line in number_of_wins:
            number_of_wins[line] += 1
        else:
            number_of_wins[line] = 1
    print(number_of_wins, end="")


##split lines function? "splitlines()"
main()