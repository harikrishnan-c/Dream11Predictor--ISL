from data.player.player import Player


class Team:

    def __init__(self, team_name, team_id):
        self.players = dict()
        self.team_name = team_name
        self.team_id = team_id

    def put_player(self, player):
        self.players[player.get_player_id()] = player

    def remove_player(self, player):
        if player.get_player_id() in self.players:
            self.players.pop(player.get_player_id())

    def get_player_count(self):
        return len(self.players)

    def get_team_name(self):
        return self.team_name

    def get_players(self):
        return self.players
