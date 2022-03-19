
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
