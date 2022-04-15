import sklearn
from scipy.cluster.hierarchy import linkage, dendrogram
import math
import random
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy.ndimage.interpolation import shift


def proj1():
    def located_delta(arr):
        max_delta = [0,0] #delta, index=
        for ele in range(1,len(arr)):
            if abs( float(arr[ele]) - float(arr[ele-1])) > max_delta[0]:
                max_delta =  [abs(float(arr[ele]) - float(arr[ele-1])), ele]
        return max_delta


    import csv
    words = open("textfiles/mlwords/words.csv")
    wordstr = str(words.read())
    word_arr = wordstr.split(",")
    meta_arr = [] #word, diffrence in corpus takeoff, most popular
    try:
        for word in word_arr:
            norm = csv.reader(open("textfiles/mlwords/"+word+"_norm.csv"))
            fict = csv.reader(open("textfiles/mlwords/"+word+"_fict.csv"))
            norm_arr = []
            fict_arr = []
            next(norm)
            next(fict)#skip headers
            for row in norm:
                norm_arr.append(row[1])
            for row in fict:
                fict_arr.append(row[1])
            meta_arr.append([word, located_delta(norm_arr),located_delta(fict_arr)])


    except FileNotFoundError:
        pass
    #print(meta_arr)
    data_arr = []
    def meta_concat(meta):
        pass

    res = list(zip(*meta_arr))
    norm_arr = np.array(res[1])
    fict_arr

    for meta in meta_arr:
        data_arr.append([meta[1][1]-meta[2][1], abs(meta[1][0]-meta[2][0])])
    from sklearn.cluster import KMeans
    c2 = np.array(data_arr)
    cluster = KMeans(n_clusters=4)
    cluster.fit(c2)
    plt.scatter(c2[:, 0], c2[:, 1], c=cluster.labels_, cmap='rainbow')
    # for l,x,y in zip(word_arr,cluster.cluster_centers_[:, 0], cluster.cluster_centers_[:, 1]):
    #     plt.annotate(l,xy=(x,y))
    for l,x,y in zip(word_arr,c2[:,0],c2[:,1]):
        plt.annotate(l,xy=(x,y))
    plt.yscale("log")
    plt.show()

#the new metric getter
def proj2():
    right_shift_years = 25
    left_shift_years = -25
    def ssd(A, B,year_offset = 0):
        A = shift(A,year_offset,cval=0)
        dif = A.ravel() - B.ravel()
        return np.dot(dif, dif)

    def conv_str_array(arr):
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        return arr

    import csv
    words = open("textfiles/mlwords/words.csv")
    wordstr = str(words.read())
    word_arr = wordstr.split(",")
    meta_arr = [] #word, diffrence in corpus takeoff, most popular
    try:
        for word in word_arr:
            norm = csv.reader(open("textfiles/mlwords/"+word+"_norm.csv"))
            fict = csv.reader(open("textfiles/mlwords/"+word+"_fict.csv"))
            norm_arr = []
            fict_arr = []
            next(norm)
            next(fict)#skip headers
            for row in norm:
                norm_arr.append(row[2])
            for row in fict:
                fict_arr.append(row[2])
            meta_arr.append([word,fict_arr,norm_arr])


    except FileNotFoundError:
        pass
    #print(meta_arr[0][1])
    data_arr = []


    for meta in meta_arr:
        try:
            # if meta[0] == "dark art":
            #     fict_arr = conv_str_array(meta[1][50:])
            #     norm_arr = conv_str_array(meta[2][50:])
            #     for i in range(len(meta[1])):
            #         farr = np.array(fict_arr) / np.amax(fict_arr)
            #         narr = np.array(norm_arr)/np.amax(norm_arr)
            #         plt.plot(farr)
            #         plt.plot(narr)
            #     plt.show()
            #     return ""
            fict_arr = conv_str_array(meta[1][50:])
            norm_arr = conv_str_array(meta[2][50:])
            scale = np.amax(fict_arr)/np.amax(norm_arr)
            min_val = None
            yrshift = 0
            #for each word, for each year, find sum of squared errors
            for i in range(left_shift_years, right_shift_years):
                val = ssd(np.array(fict_arr)/np.amax(fict_arr),np.array(norm_arr)/np.amax(norm_arr), i)
                if not min_val or val < min_val:
                    min_val = val
                    yrshift = i
            if yrshift >=0 and val < 10:
                data_arr.append([meta[0], yrshift, val])
        except ValueError:
            continue

    #plotting
    from sklearn.cluster import KMeans
    num_arr = []
    word_arr = []
    for data in data_arr:
        num_arr.append( (data[1], data[2]))
        word_arr.append(data[0])
    c2 = np.array(num_arr)
    cluster = KMeans(n_clusters=4)
    cluster.fit(c2)
    plt.scatter(c2[:, 0], c2[:, 1])
    # for l,x,y in zip(word_arr,cluster.cluster_centers_[:, 0], cluster.cluster_centers_[:, 1]):
    #     plt.annotate(l,xy=(x,y))
    # for l,x,y in zip(word_arr[:],c2[:,0],c2[:,1]):
    #     plt.annotate(l,xy=(x,y))
    #plt.yscale("log")
    plt.show()

#on demand word getter
def proj3():
    right_shift_years = 25
    left_shift_years = -25
    def ssd(A, B,year_offset = 0):
        A = shift(A,year_offset,cval=0)
        dif = A.ravel() - B.ravel()
        return np.dot(dif, dif)

    def conv_str_array(arr):
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        return arr

    import csv
    words = open("new_word.csv")
    wordstr = str(words.read())
    word_arr = wordstr.split(",")
    meta_arr = [] #word, diffrence in corpus takeoff, most popular
    try:
        for word in word_arr:
            norm = csv.reader(open("gotten_wordN.csv"))
            fict = csv.reader(open("gotten_wordF.csv"))
            norm_arr = []
            fict_arr = []
            next(norm)
            next(fict)#skip headers
            for row in norm:
                norm_arr.append(row[2])
            for row in fict:
                fict_arr.append(row[2])
            meta_arr.append([word,fict_arr,norm_arr])


    except FileNotFoundError:
        pass
    print(meta_arr[0][1])
    data_arr = []


    for meta in meta_arr:
        try:
            fict_arr = conv_str_array(meta[1][50:])
            norm_arr = conv_str_array(meta[2][50:])
            scale = np.amax(fict_arr)/np.amax(norm_arr)
            min_val = None
            yrshift = 0
            #for each word, for each year, find sum of squared errors
            for i in range(left_shift_years, right_shift_years):
                val = ssd(np.array(fict_arr)/np.amax(fict_arr),np.array(norm_arr)/np.amax(norm_arr), i)
                if not min_val or val < min_val:
                    min_val = val
                    yrshift = i
            if True:#yrshift >=0 and val < 10:
                data_arr.append([meta[0], yrshift, val])
        except ValueError:
            continue

    #plotting
    from sklearn.cluster import KMeans
    num_arr = []
    word_arr = []
    for data in data_arr:
        num_arr.append( (data[1], data[2]))
        word_arr.append(data[0])
    c2 = np.array(num_arr)
    print(c2)
    plt.scatter(c2[:, 0], c2[:, 1])
    # for l,x,y in zip(word_arr,cluster.cluster_centers_[:, 0], cluster.cluster_centers_[:, 1]):
    #     plt.annotate(l,xy=(x,y))
    for l,x,y in zip(word_arr[:],c2[:,0],c2[:,1]):
        plt.annotate(l,xy=(x,y))
    #plt.yscale("log")
    plt.show()

if __name__ == '__main__':
    proj2()
    while True:
        new_word  = input("Please input your word")
        csvfile = open("new_word.csv","w")
        csvfile.write(new_word)
        csvfile.close()
        subprocess.call("Rscript --vanilla wordgetter.r", shell=True)
        proj3()

