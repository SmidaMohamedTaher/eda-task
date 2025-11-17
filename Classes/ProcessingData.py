import pandas as pd
class ProcessingData :
    # @staticmethod
    # def getCsvData(path):
    #     return pd.read_csv(path)
    
    @staticmethod
    def getCsvData(path,sp):#sp is the separator that saaepret the column values 
        return pd.read_csv(path, sep=sp)
    
    @staticmethod
    def hotCoding(df):
        df = df.replace({"yes": 1, "no": 0})
        string_columns = df.select_dtypes(include=["object"]).columns
        return pd.get_dummies(df,columns=string_columns,dtype=int)