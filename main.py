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

not_done = True
while not_done:
  print("Which attribute would you like to see?")
  attribute = input()
  if attribute == "0":
    not_done = False
    print(username)
  elif attribute == "1":
    not_done = False
    print(password)
  elif attribute == "2":
    not_done = False
    print(score)
  elif attribute == "3":
    not_done = False
    print(highscore)
  else:
    print("Invalid input. Please input a valid attribute:")