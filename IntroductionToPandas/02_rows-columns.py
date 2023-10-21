import pandas as pd

def getDataframeSize(players):
     return [players.shape[0],players.shape[1]]
     #return [len(players),len(players.columns)]