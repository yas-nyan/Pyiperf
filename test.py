import sys
import json
import numpy as np
import matplotlib.pyplot as plt
import datetime
now =datetime.datetime.today()



def main ():
    lines = sys.stdin.read()
    # とりあえずJSONを保存しておく。
    f = open ("result/" + str(now)+".json","w")
    f.write (lines)
    print ("JSON EXPORT")
    f.close

    data = getJsonLoad(lines)

    intervals = data["intervals"]
    points = []
    rawpoints = []
    for interval in intervals:
        # intervalsのスループット部分を取り出して、単位を付けた上でpointsに流す。
        bps = interval["streams"][0]["bits_per_second"]
        rawpoints.append(bps)
        points.append (exchangeBps(bps,2))
    # print (points)

    # こっから図に書く作業
    # 最終結果を拾ってくきて最適化しとく
    avg_sent = exchangeBps( data["end"]["sum_sent"]["bits_per_second"] ,2)
    avg_recieved = data["end"]["sum_received"]["bits_per_second"]
    # x座標の範囲を書く
    x = np.arange(1,len(points)+1,1)
    print (x)
    # pointsから情報を取ってyに入れる。
    y = []
    for point in points:
        y.append(point[0])
    plt.plot(x, y,label="AVG." + str(avg_sent[0]) + avg_sent[1] )
    plt.ylabel('Throughput [Mbps]')
    plt.xlabel('TIME [s]')
    
    # 0から始まりたい
    plt.xlim(0)
    # 0から始まっていい感じにおさまるように。
    plt.ylim(0,max(y)*1.1)
    # これでMbps表示にする
    # ax.ticklabel_format(style='sci',axis='y',scilimits=(0,0)) #こいつ！！
    
    # 表示
    plt.legend(loc="best")
    plt.show()
    # 表示完了で通知
    print ("PLOT DONE")

    


def getJsonLoad (text):
    # 引数は標準出力を想定。
    try:
        data = json.loads (text)
        print ("JSON LOAD")
        return data
    except:
        print ("BAD JSON")
        return False

def exchangeBps (bps,ndigits):
    import math
    # bpsはfloat ndigitsは何位までで四捨五入だよってこと
    # 返り値pairは[値,単位]
    pair = [0,"単位"]

    if bps < 1024:
        pair[0] = round(bps,ndigits)
        pair[1] = "bps"
        return pair
    elif bps < (1024 **2):
        pair[0] = round(bps/(1024),ndigits)
        pair[1] = "Kbps"
        return pair
    elif bps < (1024 **3):
        pair[0] = round(bps/(1024 **2),ndigits)
        pair[1] = "Mbps"
        return pair
    elif bps < (1024 **4):
        pair[0] = round(bps/(1024 **3),ndigits)
        pair[1] = "Gbps"
        return pair
    else:
        pair[0] = round(bps/(1024 **4),ndigits)
        pair[1] = "ERR"
        return pair
    



if __name__ ==  "__main__":
    main()
