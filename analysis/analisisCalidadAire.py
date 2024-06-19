import pandas as pd

from generators.generadorICA import generarDatosICA

def construirDataICA():
    #creando un dataframe
    datosICA=generarDatosICA()
    dataFrameICA=pd.DataFrame(datosICA,columns=["comuna", "ica", "fecha", "id"])
    dataFrameICA.to_csv("datosica.csv", index=False)
    print(dataFrameICA)
construirDataICA()