# Create an empty list called gamers
gamers = []

# Create a function called add_gamer that takes two parameters: gamer and gamers_list. The function should check that the argument passed to the gamer parameter has both "name" and a "availability" as keys and if so add gamer to gamers_list
def add_gamer(gamer, gamers_list):
  if "name" in gamer and "availability" in gamer:
    return gamers_list.append(gamer)
  else: return "gamer data missing. Requires <name> and <availability>"
  
# Create a dictionary called kimberly with the name and availability given above.
#(info from above: Her name is Kimberly Warner and she's available on Mondays, Tuesdays, and Fridays)
# Call add_gamer with kimberly as the first argument and gamers as the second.
kimberly = {
  "name": 'Kimberly Warner',
  "availability": ["Monday", "Tuesday", "Friday"]
}
add_gamer(kimberly, gamers)

# Great! Let's add a couple more gamers to the list!
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

# Create a function called build_daily_frequency_table that takes no argument returns a dictionary with the days of the week as keys and 0s for values. We'll be using this to count the availability per night. Call build_daily_frequency_table and save the results to a variable called count_availability.
def build_daily_frequency_table():
  days = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0,
    "Saturday": 0,
    "Sunday": 0,
  }
  return days
count_availability = build_daily_frequency_table()

# Write a function called calculate_availability that takes a list of gamers as an argument gamers_list and a frequency table available_frequency. The function should iterate through each gamer in gamers_list and iterate through each day in the gamer's availability. For each day in the gamer's availability, add one to that date on the frequency table
def calculate_availability(gamers_list, available_frequency):
  for gamer in gamers_list:
    for day in gamer["availability"]:
      available_frequency[day] = available_frequency[day] + 1
  return
calculate_availability(gamers, count_availability)
# print(count_availability)

# Write a function find_best_night that takes a dictionary availability_table and returns the key with the highest number.
def find_best_night(availability_table):
  return max(availability_table, key=availability_table.get)
# print(find_best_night(count_availability))

# Call find_best_night with count_availability, store the result in a variable called game_night. Print out game_night to find out which day it is.
game_night = find_best_night(count_availability)
print(game_night)

# Create a function available_on_night that takes two parameters: gamers_list and day and returns a list of people who are available on that particular day.
# Call available_on_night with gamers and game_night and save the result into the variable attending_game_night.
# Print attending_game_night.
def available_on_night(gamers_list, day):
  attending_game_night = []
  for gamer in gamers_list:
    if day in gamer["availability"]:
      attending_game_night.append(gamer.get("name"))
  return attending_game_night

attending_game_night = available_on_night(gamers, game_night)
# print(attending_game_night)

# Define a string, called `form_email` with interpolation variables `{name}`, `{day_of_week}`, and `{game}` (in case we decide we want to use this featureset to host a different game night). Use it to tell your gaming attendees the night their Abruptly Goblins! game can be played.
form_email = "Hi {name}, on {day_of_week} we are meeting up at the comic store to play {game}! I hope you come join us! Starting at 7pm! Let's get weird!"

# Create a function send_email with three parameters: gamers_who_can_attend, day, and game. Print form_email for each gamer in gamers_who_can_attend with the appropriate day and game. Call send_email with attending_game_night, game_night, and "Abruptly Goblins!".
def send_email(gamers_who_can_attend, day, game):
  for gamer in gamers_who_can_attend:
    print(form_email.format(name=gamer, day_of_week=day, game=game))
  return

# send_email(attending_game_night, game_night, "Abruptly Goblins!")
