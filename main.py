import pandas as pd
from data.loader.masterdata import MasterDataLoader
from data.player.player import Player
from builder.team import TeamBuilder
from tabulate import tabulate


data_df = MasterDataLoader().get_master_data()

team_hyd = [ 31821,10656,23619,36329,26718,32552,38419,31842,28415,16576,25082]
team_mum = [3997, 25873, 19230, 10278, 35264, 25876, 2900, 7637, 26616, 35065, 31875]

tb = TeamBuilder(data_df,"Hyd")
tb.build_team(team_hyd)
print(tb.get_team_info())
print(print(tabulate(tb.get_players_info_df().sort_values("Rating Predicted"), headers='keys')))
# tb.get_players_info_df().to_excel("./prediction_hyd.xlsx")