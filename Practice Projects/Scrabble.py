letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

lowerc_letters = []
for letter in letters:
  lowerc_letters.append(letter.lower())

letter_to_points = {letter:point for letter, point in zip(letters, points)}
letter_to_points[" "] = 0

letter_to_points.update({letter:point for letter, point in zip(lowerc_letters, points)})

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_word("BROWNIE")


player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}


def play_word(player, word):
  player_to_words[player].append(word)



def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
      player_to_points[player] = player_points

update_point_totals()
play_word("player1", "Calipso")
update_point_totals()



print(player_to_words)
print(player_to_points)