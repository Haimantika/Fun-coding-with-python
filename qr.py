import pyqrcode
import pandas as pd


def createQRCode():


    df = pd.read_csv("Data.csv")

    for index, values in df.iterrows():

    
        number = values["number"]

        data = f'''
        number: {number} \n
        '''
        image = pyqrcode.create(data)
        image.svg(f"{number}.svg", scale="5")
        print(data)



createQRCode()
