# coding=utf-8
import csv
import os


def csv_data():
    """Reads data from csv into list of dicts
    """
    players = []

    with open('soccer_players.csv') as f:
        data = csv.DictReader(f)

        for row in data:
            player_data = dict()

            player_data['name'] = row['Name']
            player_data['height'] = row['Height (inches)']
            player_data['exp'] = row['Soccer Experience']
            player_data['guardians'] = row['Guardian Name(s)']

            players.append(player_data)

    return players


def create_league():
    """Divides 18 players into 3 leagues with same number of experienced players"""

    players = csv_data()

    # split players by experience
    exp_players = []
    inexp_players = []
    for player in players:
        if player['exp'] == 'YES':
            exp_players.append(player)
        else:
            inexp_players.append(player)

    # add experienced players to teams evenly
    exp_size = len(exp_players) / 3
    sharks = exp_players[:exp_size]
    raptors = exp_players[exp_size:(exp_size * 2)]
    dragons = exp_players[(exp_size * 2):(exp_size * 3)]

    # add inexperienced players to teams evenly
    inexp_size = len(inexp_players) / 3
    sharks.extend(inexp_players[:inexp_size])
    raptors.extend(inexp_players[inexp_size:(inexp_size * 2)])
    dragons.extend(inexp_players[(inexp_size * 2):(inexp_size * 3)])

    teams_dict = {
        'sharks': sharks,
        'raptors': raptors,
        'dragons': dragons,
    }

    return teams_dict


def teams_txt():
    """Creates the teams.txt file"""

    data = create_league()
    body_text = ''

    # create text to add to file
    for team, players in data.items():
        body_text += team.title() + "\n" + \
                     ("=" * len(team.title())) + '\n'

        for player in players:
            body_text += player['name'] + ', '
            body_text += player['exp'] + ', '
            body_text += player['guardians']

            body_text += '\n'

        body_text += '\n\n'

    # create the file
    file_name = "teams.txt"

    f = open(file_name, 'w')
    f.write(body_text)
    f.close()


def welcome_letters():
    """Creates welcome letters to players"""

    data = create_league()

    # create folder to hold letters if it doesn't exist
    folder = 'welcome_letters/'

    if not os.path.exists(folder):
        os.makedirs(folder)

    for team, players in data.items():
        for player in players:
            # create the body of the text document
            letter_text = "Dear {},".format(player['guardians']) + '\n\n'
            letter_text += "Congratulations, {} will be playing on the {} this season! ".format(
                player['name'].split(" ")[0],
                team.title())
            letter_text += "Please be there for the first practice this Sunday at 1:00pm."
            letter_text += "\n\nLooking forward to a good season!\nCoach Jordan"

            # create the file
            file_name = folder + "_".join(player['name'].lower().split(" ")) + ".txt"

            f = open(file_name, 'w')  # want each file to overwrite existing
            f.write(letter_text)
            f.close()


if __name__ == "__main__":
    teams_txt()
    welcome_letters()
