import pandas as pd

class DataFrame:
    def __init__(self, path):
        self.__df = pd.read_csv(path)

    def feat_engineer (self):
        self.__df['total_acidity'] = self.__df['fixed_acidity'] + self.__df['volatile_acidity'] + self.__df['citric_acid']
        self.__df['sugar_alcohol_ratio'] = self.__df['residual_sugar'] / self.__df['alcohol']
        self.__df['mineral_index'] = self.__df['chlorides'] + self.__df['sulphates']

        self.__df['mean_acidity'] = (self.__df['fixed_acidity'] + self.__df['volatile_acidity'] + self.__df['citric_acid']) / 3
        self.__df['total_sulfur'] = self.__df['free_sulfur_dioxide'] + self.__df['total_sulfur_dioxide']

        self.__df['alcohol_quality_interaction'] = self.__df['alcohol'] * self.__df['quality']
        self.__df['acidity_pH_balance'] = self.__df['fixed_acidity'] / self.__df['pH']

        return self.__df