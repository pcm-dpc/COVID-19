import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

class EasyDF(pd.DataFrame):
    
    def __init__(self, df):
        super().__init__(df)
    
    def select_from_column(self, col:str, lst:list):
        if lst is None:
            return self
        return self[self[col].isin(lst)]
    
    def exclude_from_column(self, col:str, lst:list):
        if lst is None:
            return self
        return self[~self[col].isin(lst)]
    
    def renormalize(self, col):
        self_num = self.select_dtypes(include=[np.number])
        tmp = self_num.divide(self[col], axis='index')
        tmp = tmp.fillna(0)
        self_copy = self.copy()
        self_copy[tmp.columns] = tmp
        return self.__class__(self_copy)
    
    def plot(self, col:str, regioni:list=None, norm:str=None):
        if regioni is None:
            hue = None
        else:
            hue = 'denominazione_regione'
        if norm is None:
            data = self.select_from_column('denominazione_regione', regioni)
        else:
            data = self.renormalize(norm).select_from_column('denominazione_regione', regioni)
        fig = plt.figure(figsize=(15,3))
        ax = sns.barplot(x="data", y=col, hue=hue, data=data)
        ax.get_xticklabels()
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        plt.legend(loc='best')
        title = col+'/'+norm if norm else col
        ax.set_title(title)
        return fig