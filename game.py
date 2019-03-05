from dateutil import parser

class Game:
	''' Processes a dict imported from the games CSV into a Game object
		with only the necessary information. 
	'''
	def __init__(self, raw_game):
		self.datetime = parser.parse(raw_game.gametime)
		self.home_team = raw_game.market
		self.away_team = raw_game.opp_market
		self.home_points = raw_game.points_game
		self.away_points = raw_game.opp_points_game

	def winning_team(self):
		if self.home_points > self.away_points:
			return self.home_team
		else:
			return self.away_team

	def losing_team(self):
		if self.home_points < self.away_points:
			return self.home_team
		else:
			return self.away_team

	def date(self):
		return self.datetime.strftime('%m/%d/%Y')

	def __repr__(self):
		return '{} {}-{} {} on {}'.format(self.home_team, self.home_points, self.away_team, self.away_points, self.date())



def df_to_games(df):
	''' Parses a Pandas Dataframe into a list of Game objects. '''
	return [Game(row) for _, row in df.iterrows()]