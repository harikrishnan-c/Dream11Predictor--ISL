from data.player.player import Player
from data.team.team import Team
import pandas as pd


class TeamBuilder:

    def __init__(self, data_df, team_name="", team_id=0):
        self.team = Team(team_name, team_id)
        self.data_df = data_df

    def build_team(self,player_id_array):
        for ids in player_id_array:
            self.team.put_player(Player(ids,self.data_df))

    def get_team_info(self):
        return " Team Info - "+self.team.get_team_name() + " " + "Player Count : " + str(self.team.get_player_count())

    def get_players_info_df(self):
        players = self.team.get_players().keys()
        df_info = pd.DataFrame(columns=["Player Name", "Player Id", "Team Name", "Position Name", "rank", "matches played", "Rating Current", "Rating Predicted"])
        list_dict = []
        for player in players:
            player_obj = self.team.get_players().get(player)
            current_rating = player_obj.get_current_rating()
            pred_rating = player_obj.predict_rating()
            position = player_obj.get_position_name()
            list_dict.append({'Player Name': player_obj.get_player_name(),
                              'Player Id': player_obj.get_player_id(),
                              'Team Name': player_obj.get_current_team_name(),
                              'Position Name': position,
                              'rank': player_obj.get_rank(),
                              'matches played': player_obj.get_matches_played(),
                              'Rating Current': current_rating,
                              'Rating Predicted': pred_rating[0]})
        df_info = df_info.append(list_dict, ignore_index=True)
        return df_info
