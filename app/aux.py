import numpy as np

def fechas_parser(fecha):
    return(
        str(fecha.year),
        "%03d" % fecha.dayofyear,
        "%02d" % fecha.hour
    )

def get_files(fs, fecha):
    '''
    El producto puede ser ABI-L2-MCMIPF o GLM-L2-LCFA
    '''
    producto = "GLM-L2-LCFA"
    return np.array(fs.ls(f'noaa-goes16/{producto}/{fechas_parser(fecha)[0]}/{fechas_parser(fecha)[1]}/{fechas_parser(fecha)[2]}/'))

def descarga_goes(fs, enlace, p_salida):
    fs.get(enlace, p_salida + enlace.split('/')[-1])