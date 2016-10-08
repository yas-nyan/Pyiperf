import sys
import json
import numpy as np
import matplotlib.pyplot as plt



def main ():
    lines = sys.stdin.read()
    data = getJsonLoad(lines)
    print (data)
    


def getJsonLoad (text):
    # 引数は標準出力を想定。
    try:
        json.load (text)
        print ("JSON LOAD")
    except:
        print ("BAD JSON")
    



if __name__ ==  "__main__":
    main()
