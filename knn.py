import os
import random
import numpy as np
import pandas as pd

tsk1 = []
import pandas as pd
import csv
from datetime import datetime,timedelta
st=383-6
end=440
date_time=datetime(2021,3,29)
for i in range(end-st):
    tp = []
    for info in os.listdir(r'C:\Users\Administrator\Desktop\0501'):
        domain = os.path.abspath(r'C:\Users\Administrator\Desktop\0501')  # 获取文件夹的路径
        info_1 = os.path.join(domain, info)  # 将路径与文件名结合起来就是每个文件的完整路径
        data = pd.read_csv(info_1)
        data.index=pd.to_datetime(data['date'])
        dataframe_1 = data.loc[data.index == date_time, ['newCasesBySpecimenDate']]


        label = 0
        tp.append([int(dataframe_1['newCasesBySpecimenDate'].values), info, label])
    date_time=date_time+timedelta(days = 1)
    tsk1.append(tp)

K = 3
l = len(tsk1[0])
for i in range(st, end):
    ini_1 = tsk1[-st + i][0][0]
    ini_2 = tsk1[-st + i][l - 1][0]
    ini_3 = (ini_1+ini_2)/2
    while True:
        for j in range(l):
            ab1 = np.abs(tsk1[-st + i][j][0] - ini_1)
            ab2 = np.abs(tsk1[-st + i][j][0] - ini_2)
            ab3 = np.abs(tsk1[-st + i][j][0] - ini_3)
            if ab1 <= ab2 and ab1 <= ab3:
                tsk1[-st + i][j][2] = 1
            else:
                if ab2 <= ab3:
                  tsk1[-st + i][j][2] = 2
                else:
                  tsk1[-st + i][j][2] = 3
        sum_1 = 0
        ct_1 = 0
        sum_2 = 0
        ct_2 = 0
        sum_3 = 0
        ct_3 = 0
        for j in range(l):
            if tsk1[-st + i][j][2] == 1:
                sum_1 = sum_1 + tsk1[-st + i][j][0]
                ct_1 = ct_1 + 1
            else:
              if tsk1[-st + i][j][2] == 2:
                sum_2 = sum_2 + tsk1[-st + i][j][0]
                ct_2 = ct_2 + 1
              else:
                sum_3 = sum_3 + tsk1[-st + i][j][0]
                ct_3 = ct_3 + 1

        if ct_1 > 0:
            mean_1 = sum_1 * 1.0 / ct_1
        else:
            mean_1 = 0
        if ct_2 > 0:
            mean_2 = sum_2 * 1.0 / ct_2
        else:
            mean_2 = 0
        if ct_3 > 0:
            mean_3 = sum_3 * 1.0 / ct_3
        else:
            mean_3 = 0
        if (np.abs(mean_1 - ini_1) < 0.1) and (np.abs(mean_2 - ini_2) < 0.1) and (np.abs(mean_3 - ini_3) < 0.1):
            break
        else:
            ini_1 = mean_1
            ini_2 = mean_2
            ini_3 = mean_3
            continue

for i in range(end-st):
    df = pd.DataFrame(tsk1[i])
df.to_csv(os.path.join('C:\\Users\\Administrator\\Desktop\\0501res_2', str(i) + '.csv'))
