import pandas as pd
import os


class MasterDataLoader:

    def __init__(self):
        self.master_data_df = pd.DataFrame(columns=['jersey_no',
                                                    'player_id',
                                                    'player_name',
                                                    'player_short_name',
                                                    'position_id',
                                                    'position_name',
                                                    'rank',
                                                    'rating',
                                                    'rating_breakup',
                                                    'team_id',
                                                    'team_name',
                                                    'team_short_name']);
        self.data_path = os.getcwd()+"/isl_data/"
        self.load_master_data()

    def load_master_data(self):
        for filename in os.listdir(self.data_path):
            with open(self.data_path+filename, 'r') as data_file:
                json_data = data_file.read()
            df_year = pd.read_json(json_data)
            self.master_data_df = pd.concat([self.master_data_df, df_year], ignore_index=True,sort=False)
            data_file.close()

    def get_master_data(self):
        return self.master_data_df
