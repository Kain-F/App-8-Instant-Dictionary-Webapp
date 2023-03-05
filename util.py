import pandas as pd

class Definition():
    def __init__(self,term):
        self.term = term

    def get(self):
        df = pd.read_csv('data.csv')
        index = pd.Index(df.word)
        res = index.get_loc(self.term)
        definition = tuple(df.loc[res].definition)
        return definition

if __name__ == ('__main__'):
    d = Definition(term='sun')
    x = d.get()
    print(x)