from .models import Result
from django.db.models import Q
import numpy as np
import csv
from .models import Result
import review.ML_model

def load_analy():

    file = str(Result.objects.values_list('Name').order_by('-pk')[0])
    file = file.replace("'", "")

    CSV_PATH = 'before_analy' + file + '.csv'
    CSV_PATH2 = 'after_analy' + file + '.csv'

    ML=review.ML_model.Analy_model()
    with open(CSV_PATH, 'r', encoding='utf-8', newline='') as csvfile:
        csv_data=[]
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            csv_data.append(row)
        csvfile.close()
    name=csv_data[0][0]
    del csv_data[0][0]
    csv_data=np.array(csv_data,dtype=np.float)
    X_test=csv_data
    after_analy=ML.predict(X_test)
    after_analy=after_analy.tolist()
    after_analy=sum(after_analy,[])
    after_analy.insert(0,name)

    if after_analy[1]==1:
        after_analy[1]='당신은 투표를 할 것입니다.'
    else:
        after_analy[1]='당신은 투표를 안 할 것입니다.'




    with open(CSV_PATH2, 'w', encoding='utf-8', newline='') as csvfile2:
        writer = csv.writer(csvfile2, delimiter=',')
        writer.writerow(['Name','D_result'])
        writer.writerow(after_analy)





