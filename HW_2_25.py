###START###

##I'm very sorry this code doesn't work, but I gave it my best shot!##

def main():
    year_won = {}
    number_of_wins = {}
    year = int(input("What year do you wanna check? "))

    infile = open("worldserieswinners.txt", "r")
    team_num_wins(infile, number_of_wins)
    assign_years(infile, year_won)

    if year == 1904 or year == 1944:
        print("Sorry, the World Series wasn't played that year.")
    else:
        if year in year_won:
            print(number_of_wins.popitem(), "won", year_won.pop(year))


def team_num_wins(infile, number_of_wins):

    winners_txt = infile.readlines()
    for line in winners_txt:
        if line in number_of_wins:
            number_of_wins[line] += 1
        else:
            number_of_wins[line] = 1


##This part COMPLETELY stumped me, Dr. B! I found a github article that
##walked through someone's solution to the problem, but I wanted to
##make it work for myself; I'm pretty sure it's wrong, ha! :) ##


def assign_years(infile, year_won):
    winner_txt = infile.readline().rstrip("\n")
    for line in winner_txt:
        for i in range(1903, 2008):
            year_won[i] = 


main()