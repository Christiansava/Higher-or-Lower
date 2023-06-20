import random
from art import logo, vs
from game_data import data
from replit import clear

#Generate a random choice from the data dictionary that was not yet chosen previously.
def random_choice(data, choices_already_selected):
  """Generate a random choice from the data dictionary that was not yet chosen previously."""

  new_choice = False
  while not new_choice:
    choice = random.choice(data)
    if choice['name'] not in choices_already_selected:
      new_choice = True

  return choice

#Calculate how has more followers, the first person or the second person generated and return the person information.
def followers(first_Person, second_Person):
  """Calculate how has more followers, the first person or the second person generated and return the person information.."""
  if first_Person['follower_count'] > second_Person['follower_count']:
    return first_Person
  else:
    return second_Person

#Analyse if the choice made by the player is the right one (person with most followers).
def winner(more_followers, choices_array, player_choice):
  """Analyse if the choice made by the player is the right one (person with most followers)."""
  choice_to_compare = choices_array[player_choice]

  if choice_to_compare == more_followers['name']:
    return 1
  else:
    return 0

#Main function that calls the other functions
def game():
  #Print logo
  print(logo)

  #Define some variables
  choices_array = {}
  score = 0
  end_game = True
  choices_already_selected = []

  #Choose the first person for comparison and append it to the array that keeps track of the persons that were already selected
  first_Person = random_choice(data, choices_already_selected)
  choices_already_selected.append(first_Person['name'])
  
  #While loop to keep chossing more persons to compare if player has got everything right.
  while end_game:

    #Choose second person to compare and add the person to the array that keeps track.
    second_Person = random_choice(data, choices_already_selected)
    choices_already_selected.append(second_Person['name'])

    #Print some information from both persons that we are comparing and als the VS logo
    print(f"Compare A: {first_Person['name']}, {first_Person['description']}, from {first_Person['country']}.")
    print(vs)
    print(f"Against B: {second_Person['name']}, {second_Person['description']}, from {second_Person['country']}.")

    #Register both choices on an dictionary and assiciate each one to the letters A and B
    choices_array = {'A': first_Person['name'], 'B': second_Person['name']}
    
    #Ask the user to choose who he tinks has the most followers on instagram
    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    #Calculate who has more followrs, First Person or Second Person.
    more_followers = followers(first_Person, second_Person)

    #Obtain the result based on players choice and person with more followers
    result = winner(more_followers, choices_array, player_choice)
    clear()
    print(logo)
    #Calculate score and understand if the game should continue or if the player has lost
    if result == 1:
      score += 1
      print(f"You're right! Current score: {score}")
      first_Person = second_Person
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      end_game = False

#Calling the main function
game()
