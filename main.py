import pandas as pd
from data.loader.masterdata import MasterDataLoader
from data.player.player import Player
from builder.team import TeamBuilder
from tabulate import tabulate


data_df = MasterDataLoader().get_master_data()

# team_hyd = [ 31821,10656,23619,36329,26718,32552,38419,31842,28415,16576,25082]
# team_mum = [3997, 25873, 19230, 10278, 35264, 25876, 2900, 7637, 26616, 35065, 31875]
team_goa = [31773, 39013, 32054, 55658, 19152, 10708, 9569, 55648, 31824, 10255, 19141, 26611, 32021, 18821, 10689, 31847, 55653, 31791, 36832, 35062]
team_ker = [55652, 11205, 68806, 5213, 36860, 17683, 27025, 34002, 35298, 55646, 10770, 19130, 69285, 10682, 31882, 67615, 34007, 28324, 10252, 36603, 16558, 35194, 10644]

tb = TeamBuilder(data_df,"All")
tb.build_team(team_goa)
print(tb.get_team_info())
print(print(tabulate(tb.get_players_info_df().sort_values("Rating Predicted"), headers='keys')))
tb.get_players_info_df().to_excel("./prediction_ker_players_vs_goa_all.xlsx")
# df_goa = data_df[data_df["team_id"]==498]
# print(print(tabulate(df_goa, headers='keys')))
# print(list(df_goa["player_id"].values))
