def solve(games):
	''' Solves the Circle of Defeat problem.

	Takes a list of Game objects as input.

	Returns an ordered list that represents a solution. '''

	# Store a dictionary where keys are teams and values are lists of the teams they've beaten.
	won_games = {}
	def update_dict(winning_team, game):
		if winning_team not in won_games:
			won_games[winning_team] = set()
		won_games[winning_team].add(game)

	# Fill this dictionary
	for game in games:
		update_dict(game.winning_team(), game)

	won_games['Pittsburgh'] = set() # lol

	num_acc_teams = len(won_games.keys()) 
	
	# Do a depth-first search
	start_team = next(iter(won_games))
	team_names_seen = []
	circle = [] # same as team_names_seen but Game objects
	Q = [start_team]
	def find_circle(path, path_team_names, team):
		# if circle complete, stop
		if len(circle):
			return
		# Pitt did not win any games
		if team == 'Pittsburgh': 
			return
		# team already in circle, can't add it again
		if team in path_team_names:
			return
		# iterate through the teams defeated by `team`
		for won_game in won_games[team]:
			if len(path) == num_acc_teams - 1 - 1: # - 1 for pitt
				if won_game.losing_team() == start_team:
					circle.extend(path + [won_game])
					return
			find_circle(path + [won_game], path_team_names + [team], won_game.losing_team()) 
	find_circle([], [], start_team)
	# Return result
	return circle