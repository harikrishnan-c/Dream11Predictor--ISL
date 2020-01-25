import pandas as pd
from statsmodels.tsa.arima_model import ARIMA


class Player:

    def __init__(self, player_id, data_df):
        self.player_id = player_id
        self.player_df = data_df[data_df["player_id"] == player_id]
        self.position = self.player_df.iloc[len(self.player_df)-1]["position_name"]
        self.player_name = self.player_df.iloc[len(self.player_df)-1]["player_name"]
        self.current_team = self.player_df.iloc[len(self.player_df)-1]["team_name"]
        self.rank = self.player_df.iloc[len(self.player_df)-1]["rank"]
        self.matches_played = 0
        self.df_rating_breakup = pd.DataFrame(columns=['match_date',
                                                       'match_id',
                                                       'rating',
                                                       'vs_team_id',
                                                       'vs_team_name',
                                                       'vs_team_short_name'])
        self.training_df = pd.DataFrame()
        self.build_player_rating_breakup()
        self.build_rating_df()

    def build_player_rating_breakup(self):
        for entry in self.player_df["rating_breakup"]:
            df_player_rating = pd.read_json(str(entry).replace("\'", "\""))
            self.df_rating_breakup = pd.concat([self.df_rating_breakup, df_player_rating], ignore_index=True,sort=True)
        self.df_rating_breakup["match_date"] = pd.to_datetime(self.df_rating_breakup["match_date"],
                                                              format='%m/%d/%Y %H:%M:%S PM')

    def build_rating_df(self):
        self.training_df = self.df_rating_breakup[["match_date", "rating"]]
        self.training_df.set_index('match_date', inplace=True)

    def predict_rating(self):
        try:
            X = self.training_df.values
            model = ARIMA(X, order=(0,0,1))
            model_fit = model.fit(disp=0)
            output = model_fit.forecast()
            yhat = output[0]
        except:
            print("Algorithm Failed for :"+self.player_name)
            yhat = [0.0]
        return yhat

    def get_player_id(self):
        return self.player_id

    def get_current_rating(self):
        try:
            return self.training_df.iloc[len(self.training_df)-1]['rating']
        except:
            return 0.0
        return

    def get_player_name(self):
        return self.player_name

    def get_current_team_name(self):
        return self.current_team

    def get_position_name(self):
        return self.position

    def get_rank(self):
        return self.rank

    def get_matches_played(self):
        return self.df_rating_breakup.shape[0]
