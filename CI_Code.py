import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tkinter import messagebox

data = pd.read_csv('IrisData.txt')
X=data.iloc[0:150 , 0:4]
W=[]
Y=data["Class"]
x_set=[]
x_versi=[]
y_Plist=[]
totalX_train=[]
totalY_train=[]
totalY_test=[]
totalX_test=[]
resultX_train=[]
resultY_train=[]
resultX_test=[]
resultY_test=[]
flag0=""
flag1=""
checkRead=0
def InputData(XTr1,XTr2,YTr1,YTr2,XTs1,XTs2,YTs1,Yts2):
    global resultX_train
    global resultY_train
    global resultX_test
    global resultY_test
    totalX_train = [XTr1, XTr2]
    totalY_train = [YTr1, YTr2]
    totalX_test = [XTs1, XTs2]
    totalY_test = [YTs1, Yts2]
    resultX_train = pd.concat(totalX_train)
    resultY_train = pd.concat(totalY_train)
    resultX_test = pd.concat(totalX_test)
    resultY_test = pd.concat(totalY_test)
def Read(ft1,ft2,classes):
    if ft1==ft2:
        msg=messagebox.showinfo("Error","Please choose different features")
        return
    global x_set
    global checkRead
    global x_versi
    global totalX_train
    global totalY_train
    global totalX_test
    global totalY_test
    global flag0
    global flag1
    global resultX_train
    global resultY_train
    global resultX_test
    global resultY_test
    checkRead=1
    y_set = Y.iloc[0:50]
    y_versi = Y.iloc[50:100]
    y_virgi = Y.iloc[100:150]

    if classes=="C1&C2":
        flag0="Iris-setosa"
        flag1="Iris-versicolor"
        if((ft1=='X1' and ft2=='X2')or (ft1=='X2' and ft2=='X1')):
           x_set=X.iloc[0:50,0:2]
           # print(x_set.iloc[0,0])
           # print(x_set.iloc[1, 0])
           # print(x_set)
           x_versi=X.iloc[50:100,0:2]
        if((ft1=='X1' and ft2=='X3')or(ft1=='X3' and ft2=='X1')):
            x_set = X.iloc[0:50, 0::2]
            x_versi =X.iloc[50:100, 0::2]
        if ((ft1 == 'X1' and ft2 == 'X4') or (ft1 == 'X4' and ft2 == 'X1')):
            x_set = X.iloc[0:50, 0::3]

            x_versi=X.iloc[50:100, 0::3]
        if ((ft1 == 'X2' and ft2 == 'X3') or (ft1 == 'X3' and ft2 == 'X2')):
            x_set = X.iloc[0:50, 1:3]
            x_versi = X.iloc[50:100, 1:3]
        if ((ft1 == 'X2' and ft2 == 'X4') or (ft1 == 'X4' and ft2 == 'X2')):
            x_set = X.iloc[0:50, 1::2]
            x_versi = X.iloc[50:100, 1::2]
        if ((ft1 == 'X3' and ft2 == 'X4') or (ft1 == 'X4' and ft2 == 'X3')):
            x_set = X.iloc[0:50, 2:4]
            x_versi = X.iloc[50:100, 2:4]
        x_train_set, x_test_set, y_train_set, y_test_set = train_test_split(x_set, y_set, train_size=30, test_size=20,shuffle=False)
        x_train_versi, x_test_versi, y_train_versi, y_test_versi = train_test_split(x_versi, y_versi, train_size=30, test_size=20,shuffle=False)
        InputData(x_train_set,x_train_versi,y_train_set,y_train_versi,x_test_set,x_test_versi,y_test_set,y_test_versi)
        #x_set=x_set.assign(x0=pd.Series(1),index=1)


        # [1, 2]
        # [3, 4]
        # print("---------------------------------------X_train-----------------------------")
        # print(totalX_train.__getitem__(0))
        # print("---------------------------------------Y_train-----------------------------")
        # print(totalY_train)
        # print("---------------------------------------X_test-----------------------------")
        # print(totalX_test)
        # print("---------------------------------------Y_test-----------------------------")
        # print(totalY_test)

    elif classes=="C1&C3":
        if((ft1=='X1' and ft2=='X2')or (ft1=='X2' and ft2=='X1')):
           x_set=X.iloc[0:50,0:2]
           x_virgi=X.iloc[100:150,0:2]
        if((ft1=='X1' and ft2=='X3')or(ft1=='X3' and ft2=='X1')):
            x_set = X.iloc[0:50, 0::2]
            x_virgi=X.iloc[100:150, 0::2]
        if ((ft1 == 'X1' and ft2 == 'X4') or (ft1 == 'X4' and ft2 == 'X1')):
            x_set = X.iloc[0:50, 0::3]
            x_virgi=X.iloc[100:150, 0::3]
        if ((ft1 == 'X2' and ft2 == 'X3') or (ft1 == 'X3' and ft2 == 'X2')):
            x_set = X.iloc[0:50, 1:3]
            x_virgi = X.iloc[100:150, 1:3]
        if ((ft1 == 'X2' and ft2 == 'X4') or (ft1 == 'X4' and ft2 == 'X2')):
            x_set = X.iloc[0:50, 1::2]
            x_virgi = X.iloc[100:150, 1::2]
        if ((ft1 == 'X3' and ft2 == 'X4') or (ft1 == 'X4' and ft2 == 'X3')):
            x_set = X.iloc[0:50, 2:4]
            x_virgi = X.iloc[100:150, 2:4]
        x_train_set, x_test_set, y_train_set, y_test_set = train_test_split(x_set, y_set, train_size=30, test_size=20,shuffle=False)
        x_train_virgi, x_test_virgi, y_train_virgi, y_test_virgi = train_test_split(x_virgi, y_virgi, train_size=30, test_size=20,shuffle=False)
        InputData(x_train_set,x_train_virgi,y_train_set,y_train_virgi,x_test_set,x_test_virgi,y_test_set,y_test_virgi)
        # print(totalX_train)

        # print("****************************************")
        # print(resultX_train)
        # totalX_train = [x_train_set, x_train_virgi]
        # totalY_train = [y_train_set, y_train_virgi]
        # totalX_test = [x_test_set , x_test_virgi]
        # totalY_test = [y_test_set , y_test_virgi]
        # resultX_train = pd.concat(totalX_train)
        # resultY_train = pd.concat(totalY_train)
        # resultX_test = pd.concat(totalX_test)
        # resultY_test = pd.concat(totalY_test)
        # print("---------------------------------------X_train-----------------------------")
        # print(totalX_train)
        # print("---------------------------------------Y_train-----------------------------")
        # print(totalY_train)
        # print("---------------------------------------X_test-----------------------------")
        # print(totalX_test)
        # print("---------------------------------------Y_test-----------------------------")
        # print(totalY_test)

    elif classes=="C2&C3":

        if((ft1=='X1' and ft2=='X2')or (ft1=='X2' and ft2=='X1')):
           x_versi=X.iloc[50:100,0:2]
           x_virgi=X.iloc[100:150,0:2]
        if((ft1=='X1' and ft2=='X3')or(ft1=='X3' and ft2=='X1')):
            x_versi = X.iloc[50:100, 0::2]
            x_virgi=X.iloc[100:150, 0::2]
        if ((ft1 == 'X1' and ft2 == 'X4') or (ft1 == 'X4' and ft2 == 'X1')):
            x_versi = X.iloc[50:100, 0::3]
            x_virgi=X.iloc[100:150, 0::3]
        if ((ft1 == 'X2' and ft2 == 'X3') or (ft1 == 'X3' and ft2 == 'X2')):
            x_versi = X.iloc[50:100, 1:3]
            x_virgi = X.iloc[100:150, 1:3]
        if ((ft1 == 'X2' and ft2 == 'X4') or (ft1 == 'X4' and ft2 == 'X2')):
            x_versi = X.iloc[50:100, 1::2]
            x_virgi = X.iloc[100:150, 1::2]
        if ((ft1 == 'X3' and ft2 == 'X4') or (ft1 == 'X4' and ft2 == 'X3')):
            x_versi = X.iloc[50:100, 2:4]
            x_virgi = X.iloc[100:150, 2:4]
        x_train_virgi, x_test_virgi, y_train_virgi, y_test_virgi = train_test_split(x_virgi, y_virgi, train_size=30, test_size=20,shuffle=False)
        x_train_versi, x_test_versi, y_train_versi, y_test_versi = train_test_split(x_versi, y_versi, train_size=30, test_size=20,shuffle=False)
        InputData(x_train_virgi, x_train_versi, y_train_virgi, y_train_versi, x_test_virgi, x_test_versi, y_test_virgi,y_test_versi)
        # totalX_train = [x_train_versi,x_train_virgi]
        # totalY_train = [ y_train_versi,y_train_virgi]
        # totalX_test = [x_test_versi,x_test_virgi]
        # totalY_test = [y_test_versi,y_test_virgi]
        # resultX_train = pd.concat(totalX_train)
        # resultY_train = pd.concat(totalY_train)
        # resultX_test = pd.concat(totalX_test)
        # resultY_test = pd.concat(totalY_test)
        # print("---------------------------------------X_train-----------------------------")
        # print(totalX_train)
        # print("---------------------------------------Y_train-----------------------------")
        # print(totalY_train)
        # print("---------------------------------------X_test-----------------------------")
        # print(totalX_test)
        # print("---------------------------------------Y_test-----------------------------")
        # print(totalY_test)
    msg=messagebox.showinfo("Done","Data is Ready")
def calc(y_pred,val,W,alpha,arr):
    print(y_pred)
    print("----Y",val)
    # error=None
    if y_pred != val:
        print("change")
        error = val-y_pred
        #newarr=[i*(alpha * error) for i in arr]
        W = W +alpha * error*arr

    return W
# def enhanceW(error,y_pred,val,W,alpha,arr):
#     while error!=0:
#         error = val - y_pred
#         W = W + np.dot((alpha * error), arr)
#         y_pred = signum(np.dot(W, arr))
#         print("Error",error)
   # return W


def signum(y_pred):
    x=0
    if y_pred<0:
        x=-1
    elif y_pred>0:
        x=1
    return x
def learn(epochs, x_Train ,  y_train , bias , alpha ):
    # if checkRead==0:
    #     msg = messagebox.showinfo("Error", "Please Read first")
    #     return
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    global W
    if bias=="1":
        x_Train["X0"]=1
            # print(x_Train)
    else:
        x_Train["X0"]=0
    W = np.random.uniform(low=-2, high=2, size=(1, 3))
    print("OldW")
    print(W)
    #print(x_Train)
    #flag=0
    arr=[]
    #count=0
    for i in range(epochs):
        for j in range(len(x_Train)):
            for k in x_Train.iloc[j,:]:
                arr.append(k)
            arr2=np.array(arr)
            y_pred = signum(np.dot(W, arr2))
            if j<len(x_Train)/2:
                W=calc(y_pred,1,W,alpha,arr2)
            elif j>=len(x_Train)/2 :
                W=calc(y_pred, -1, W, alpha, arr2)
            arr.clear()
            #count=count+1

    #     for j in x_Train:
    #
    #         row = 0
    #         for k in j.iloc[row, :]:
    #             arr.append(k)
    #             row=row+1
    #     y_pred =  np.dot(W ,arr)  + bias
    #
    #                 if y_pred > 0:
    #                     y_pred = 1
    #                 else :
    #                     y_pred = -1
    #                 if flag==0:
    #                     calc(y_pred,1,W,alpha,k)
    #                 elif flag==1:
    #                     calc(y_pred,-1,W,alpha,k)
    #     flag=1
    # print(x_Train)
    print("finalW")
    print(W)
    msg = messagebox.showinfo("Done", "Data is Ready to be Tested")



# Read("X3","X4","C1&C3")
# print(totalX_train.__getitem__(1).iloc[0,0])
# print(totalX_train)
# Read("X1","X2","C1&C2")
# print(totalX_train)
# print("------------------------------------------------")
# arr=[1,5]
# arr2=np.reshape(arr,(2,1))
# print(arr)
# print("-------------")
# print(arr2)
# print("----------")
# print(totalX_train)
# print("----------")
# arrx=[]
# f = 0
# for j in totalX_train:
#
#     for k in j.iloc[0,:]:
#         print(k)
#         arrx.append(k)
#     break
#
#         #print(np.dot(k,arr2))
#
#
# print(arrx)
def test(x_test,W,y_test,bias):

    confusion=[0,0,0,0]
    confusionMatrix1=np.array(confusion)
    confusionMatrix=np.reshape(confusionMatrix1,(2,2))
    global y_Plist
    y_Plist.clear()
    print(y_test)

    if bias=="1":
        x_test["X0"]=1
    else:
        x_test["X0"]=0
    print(x_test)
    vartrue=0
    arr=[]
    #nW = np.reshape(W,(3,1))
    #print(nW.shape)
    for i in range(len(x_test)):
        print(x_test)
        for k in x_test.iloc[i, :]:

            arr.append(k)
            print(arr)
        print(arr)

        y_pred = signum(np.dot(W, arr))
        y_Plist.append(y_pred)
        print("----------------------W------------------------")
        print(W[0])
        print("----------------------dot------------------")
        print(np.dot(W, arr))
        arr.clear()
    for j in range(len(y_test)):
        if j<len(y_test)/2:
            if y_Plist[j]==1:
                vartrue=vartrue+1
                confusion[0]=confusion[0]+1
            else:
                confusion[1]=confusion[1]+1
        else:
            if y_Plist[j]==-1:
                vartrue=vartrue+1
                confusion[2] = confusion[2] + 1
            else:
                confusion[3] = confusion[3] + 1
        confusionMatrix = np.reshape(confusion, (2, 2))
    print(vartrue)
    print(len(y_test))
    acc=(vartrue/len(y_test))
    print("accuracy= ",acc)
    msg = messagebox.showinfo("Test Done", "Your accuracy is {}% \n confusion Matrix=\n{}".format(acc*100,confusionMatrix))
