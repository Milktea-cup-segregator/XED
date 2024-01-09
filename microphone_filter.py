import Kalman_Filter

tmp = 150

noisePoint=150
if tmp<noisePoint:
    tmp=Kalman_Filter.kalman(tmp)


