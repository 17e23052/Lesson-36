players = []

add_players = True
while add_players:
    print("Enter a username:")
    username = input()
    print("Enter a password:")
    password = input()
    print("Enter a score")
    score = input()
    print("Enter your highest score:")
    highscore = input()

    player = {"username" : username,
              "password" : password,
              "score" : score,
              "highscore": highscore}

    players.append(player)

    print("Would you like to add another player? Y/N")
    answer = input().upper()
    if answer == "N":
        add_players = False

print(players)
print(password)