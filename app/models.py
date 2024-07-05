from aux import *
import s3fs
import numpy as np
import pandas as pd
from multiprocessing import Pool, set_start_method

#---------------------------------------------------------
# Vars
fini = "2020-04-02T06:00:00" 
ffin = "2020-04-02T08:00:00" 
n_cores = 10
path_salida = "downloads/"

#---------------------------------------------------------
def getAbi(fini, ffin, n_cores, path_salida):
    rango_fechas = pd.date_range(pd.to_datetime(fini), pd.to_datetime(ffin), freq="h")
    fs = s3fs.S3FileSystem(anon=True)
    if __name__ == '__main__':
        set_start_method('spawn')  # establece el método de inicio a 'spawn'
        ## obtención de la lista de imagenes disponibles en el rango de fechas
        with Pool(n_cores) as pool:
            args = [(fs, a) for a in rango_fechas]
            files_list = pool.starmap(get_files, args)
        files = np.concatenate(files_list, axis = 0)
        ## descarga de imagenes a local
        with Pool(n_cores) as pool:
            args = [(fs, a, path_salida) for a in files]
            pool.starmap(descarga_goes, args)

def main():
    getAbi(fini, ffin, n_cores, path_salida)

if __name__ == "__main__":
    main()