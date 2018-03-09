import csv

def get_data():
    player_data = {
        'name': [],
        'height': [],
        'exp': [],
        'guardians': [],
    }

    with open('soccer_players.csv', newline='') as f:
        csv_data = csv.DictReader(f)

        for row in csv_data:
            teams['name'].append(row['Name'])
            teams['height'].append(row['Height (inches)'])
            teams['exp'].append(row['Soccer Experience'])
            teams['guardians'].append(row['Guardian Name(s)'])

    return player_data

def create_league():
    """divide 18 players into 3 leagues with same number of experienced players"""

    players = get_data()

    data_list = list(csv_data)

    team_size = len(data_list)/len(teams)

    sharks = {}
    dragons = {}
    raptors = {}


def welcome_letters():
    """to create welcome letters to players"""

    players = get_data()

    for player in players:

        # create the body of the text document
        letter_text = "Dear, {}".format(players['guardians'])
        letter_text += "Congratulations, {} will be playing on the {} this season!".format(players['name'], players['team_name'])
        letter_text += "Please be there for the first practice on {}".format(players['guardians'])
        letter_text += "\n\nLooking forward to a good season!\nCoach Jordan"

        # create the file
        file_name = "_".join(players['name'].split()) + ".txt"

        file = open(file_name, ”w”)
        file.write(letter_text)
        file.close()

    # EXTRA CREDIT:

    # Create 18 text files ("welcome" letters to the players' guardians).
    # You'll create 1 text file for each player. Use the player’s name as the name of the file, in lowercase and with underscores and ending in .txt.
    # For example, kenneth_love.txt.
    # Make sure that each file begins with the text "Dear" followed by the guardian(s) name(s).
    # Also include the additional required information: player's name, team name, and date & time of first practice.

if __name__ == "__main__":
    create_league()
    welcome_letters()
