import pandas as pd

class File:
    def __init__(self):
        self.file = None

    def Excel(self, Filepath):
        a = pd.read_excel(Filepath)  
        self.file = a
        return a

    def Csv(self, Filepath):
        a = pd.read_csv(Filepath)
        self.file = a
        return a

    def JSON(self, Filepath):
        a = pd.read_json(Filepath)
        self.file = a
        return a
    
    def avrege(self):
            avr=self.file.mean()
            return avr
        
    def mostFrequentValues(self):
        mode=self.file.mode
        return mode
    def dropNull(self,axis):
        self.file=self.file.dropna(axis=axis)
    def fullNull(self,value,axis):
        self.file=self.file.fillna(value=value,axis=axis)
file_instance = File()

file_instance.Csv("C:\\Users\\ALARABIYA\\Desktop\\github\\Salary.csv")

