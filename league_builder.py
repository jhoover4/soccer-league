# coding=utf-8
import csv
import os

def csv_data():
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
    """divide 18 players into 3 leagues with same number of experienced players"""

    players = csv_data()

    exp_players = []
    non_exp_players = []

    for player in players:
        if player['exp'] == 'YES':
            exp_players.append(player)
        else:
            non_exp_players.append(player)

    # split up experienced players
    exp_size = len(exp_players) / 3
    sharks = exp_players[:exp_size]
    raptors = exp_players[exp_size:(exp_size * 2)]
    dragons = exp_players[(exp_size * 2):(exp_size * 3)]

    # split up un-experienced players
    non_exp_size = len(non_exp_players) / 3
    sharks.extend(non_exp_players[:non_exp_size])
    raptors.extend(non_exp_players[non_exp_size:(non_exp_size * 2)])
    dragons.extend(non_exp_players[(non_exp_size * 2):(non_exp_size * 3)])

    teams_dict = {
        'sharks': sharks,
        'raptors': raptors,
        'dragons': dragons,
    }

    return teams_dict


def teams_txt():
    """Create the teams.txt file"""

    data = create_league()
    body_text = ''

    # create text to add to file
    for team, players in data.items():
        body_text += team.title() + '\n'

        for player in players:
            body_text += player['name'] + ', '
            body_text += player['exp'] + ', '
            body_text += player['guardians']

            body_text += '\n'

        body_text += '\n'

    # create the file
    file_name = "teams.txt"

    f = open(file_name, 'a')
    f.write(body_text)
    f.close()


def welcome_letters():
    """to create welcome letters to players"""

    data = create_league()

    # create folder to hold letters if it doesn't exist
    folder = 'welcome_letters/'

    if not os.path.exists(folder):
        os.makedirs(folder)


    for team, players in data.items():
        for player in players:

            # create the body of the text document
            letter_text = "Dear {},".format(player['guardians']) + '\n\n'
            letter_text += "Congratulations, {} will be playing on the {} this season! ".format(player['name'].split(" ")[0],
                                                                                               team.title())
            letter_text += "Please be there for the first practice this Sunday at 1:00pm."
            letter_text += "\n\nLooking forward to a good season!\nCoach Jordan"

            # create the file
            file_name = folder + "_".join(player['name'].lower().split(" ")) + ".txt"

            f = open(file_name, 'w') # want each file to overwrite existing
            f.write(letter_text)
            f.close()


if __name__ == "__main__":
    teams_txt()
    welcome_letters()
