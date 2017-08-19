import re
import numpy as np
import numpy.ma as ma

nx = 360; ny = 180
lon = -179.5 + np.arange(nx)
lat = 89.5 - np.arange(ny)

def readtxt(fname, m):
    fin = open(fname, 'rt')
    sst = ma.zeros((m, ny, nx))
    land = -32768
    seaice = -1000
    for k in range(m):
        fin.readline()
        for j in range(ny):
            line = re.sub(str(land), ' '+str(seaice), fin.readline())
            sst[k, j, :] = ma.masked_equal(np.array(line.split()).astype(int), seaice) * 0.01
    fin.close()
    return sst
