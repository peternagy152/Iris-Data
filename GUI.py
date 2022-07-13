from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import CI_Code
import numpy as np

data=pd.read_csv("IrisData.txt")

classes=data["Class"]




form1=Tk()
form1.geometry("720x500")
info1=StringVar()
info2=StringVar()
classes_info=StringVar()
bias_info=StringVar()
Learning_info=StringVar()
epochs_info=StringVar()
var1=None
var2=None
classes_combo=None
learningrate=None
epochs=None
check_box=None
X3=None
def CreateInputFeatures(labeltxt,lablx,lably,combox,comboy,curr,var,op,info=StringVar()):
    l1 = Label(form1, text=labeltxt)
    l1.place(x=lablx, y=lably)
    var = ttk.Combobox(form1, width=10,state="readonly",textvariable=info)
    var.grid(column=1, row=0)
    var.place(x=combox, y=comboy)
    ComboGenerateValues(var,op)
    var.current(curr)
def ComboGenerateValues(var,op):
    if op==0:
        var["values"]=["X1","X2","X3","X4"]
    else:
        var["values"] = ["C1&C2", "C1&C3", "C2&C3"]
# def CreateInputClasses(labeltxt,lablx,lably,combox,comboy,curr,var,info=StringVar()):
#     l1 = Label(form1, text=labeltxt)
#     l1.place(x=lablx, y=lably)
#     var = ttk.Combobox(form1, width=10,state="readonly",textvariable=info)
#     var.grid(column=1, row=0)
#     var.place(x=combox, y=comboy)
#
#     var.current(curr)
def CreateEpochs_LE(labeltxt,labelx,lably,entryx,entryY,e,info=StringVar()):
    l=Label(form1,text=labeltxt)
    l.place(x=labelx,y=lably)
    e=Entry(form1, textvariable=info)
    e.place(x=entryx,y=entryY)
def Create_bias(labeltxt,check_x,check_y,check_box,info=StringVar()):
    check_box=Checkbutton(form1, text = labeltxt, variable = info, onvalue = "1", offvalue="0")
    check_box.place(x=check_x,y=check_y)
    check_box.deselect()
def Plot():
    if info1.get()==info2.get():
        msg=messagebox.showinfo("Error","Please choose different features")
        return
    X1 = data[info1.get()]
    X2 = data[info2.get()]
    plt.scatter(X1.iloc[0:50],X2.iloc[0:50],label="C1")
    plt.scatter(X1.iloc[51:100],X2.iloc[51:100],label="C2")
    plt.scatter(X1.iloc[101:151], X2.iloc[101:151],label="C3")
    plt.legend()
    plt.show()
    # print(X1)
    # print("======================================")
    # print(X1.iloc[0:51])


    #plt.figure("fig1")
    #plt.scatter()


CreateInputFeatures("Feature 1 :",10,10,70,10,0,var1,0,info1)
CreateInputFeatures("Feature 2 :",200,10,260,10,1,var2,0,info2)
CreateInputFeatures("Classes",10,40,70,40,0,classes_combo,1,classes_info)
CreateEpochs_LE("Learning Rate :",10,80,100,80,learningrate,Learning_info)
CreateEpochs_LE("Epochs :",10,110,100,110,epochs,epochs_info)
Create_bias("Bias",10,130,check_box,bias_info)
def testfn():
    print(info1.get())
    print(info2.get())
    print(classes_info.get())
    print(Learning_info.get())
    print(epochs_info.get())
    print(bias_info.get())

# b=Button(form1,text="test",command=testfn)
# b.place(x=10,y=150)
b2=Button(form1,text="Show",command=Plot)
b2.place(x=10,y=200)



def PlotLine(W):
    #print(W[0,0])
   # strW=str(W)
   # nW=strW.split()
    X1 = data[info1.get()]
    X2 = data[info2.get()]
    X = []
    Y = []
    x1 = 0
    y2 = 0
    x2 = -W[0, 2] / W[0, 0]
    y1 = -W[0, 2] / W[0, 1]
    X.append(x1)
    X.append(x2)
    Y.append(y1)
    Y.append(y2)
    # m=-(W[0,2]/W[0,1])/(W[0,2]/W[0,0])
    # c=-W[0,2]/W[0,1]
    # plt.legend([X,X], loc = 0)
    # plt.plot(X,Y)
    # # plt.axis()
    #plt.plot(X, Y)
   # form1,ax = plt.subplots()
    if classes_info.get()=="C1&C2":
        plt.scatter(X1.iloc[0:50], X2.iloc[0:50], label="C1")
        plt.scatter(X1.iloc[50:100], X2.iloc[50:100], label="C2")
    elif classes_info.get()=="C1&C3":
        plt.scatter(X1.iloc[0:50], X2.iloc[0:50], label="C1")
        plt.scatter(X1.iloc[100:150], X2.iloc[100:150], label="C3")
    else:
        plt.scatter(X1.iloc[50:100], X2.iloc[50:100], label="C2")
        plt.scatter(X1.iloc[100:150], X2.iloc[100:150], label="C3")
    #ax.scatter(X1.iloc[101:151], X2.iloc[101:151], label="C3")
    plt.axline((X[0],Y[0]),(X[1],Y[1]),color='C3', label='by points')
    # axes = plt.axis()
    # plt.plot([X[-2], X[-2] + 1000 * (X[-1] - X[-2])], [Y[-2], Y[-2] + 1000 * (Y[-1] - Y[-2])])
    # plt.xlim([axes[0], axes[1]])
    # plt.ylim([axes[2], axes[3]])
    nX=np.array(X)
    # plt.plot(X,m*nX+c)
    plt.show()




readbtn=Button(form1,text="Read Data",command=lambda :CI_Code.Read(info1.get(),info2.get(),classes_info.get()))
readbtn.place(x=10,y=300)

# print(type(Learning_info.get()))
learnbtn=Button(form1,text="Learn",command=lambda :CI_Code.learn(int(epochs_info.get()),CI_Code.resultX_train,CI_Code.resultY_train,bias_info.get(),float(Learning_info.get())))
learnbtn.place(x=150,y=300)
testbtn=Button(form1,text="test",command=lambda :CI_Code.test(CI_Code.resultX_test,CI_Code.W,CI_Code.resultY_test,bias_info.get()))
testbtn.place(x=250,y=300)
drawline=Button(form1,text="Draw",command=lambda :PlotLine(CI_Code.W))
drawline.place(x=400,y=400)
form1.mainloop()
#CI_task_Code.ReadData(info1.get(),info2.get(),classes_info.get())
