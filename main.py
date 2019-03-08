import pandas as pd
from game import df_to_games
from circle_of_defeat import solve
from make_circle_image import show_game_circle

def main():
	# Convert games CSV to dataframe.
	game_df = pd.read_csv('ncaa_acc_2017_games.csv')
	# Parse dataframe to Game objects.
	games = df_to_games(game_df) 
	# Solve the problem.
	solution = solve(games)
	# Show the Circle of Defeat image.
	show_game_circle(solution)
	# Output your solution in an understandable format.
	for game in solution:
		print(game.winning_team(),'beat',game.losing_team(),'on', game.date())

main()