import pickle
from tkinter import *
import warnings
warnings.filterwarnings('ignore')
from PIL import Image,ImageTk
dt = pickle.load(open('dt.pkl', 'rb'))  
rf = pickle.load(open('RF.pkl', 'rb'))

root = Tk()
root.title('ADHD prediction system')
root.geometry('1500x800')
root.configure(background="#d1b4b4")
img=Image.open("aa.jpg")
img=img.resize((1500,755))
bg=ImageTk.PhotoImage(img)

lbl=Label(root,image=bg)
lbl.place(x=0,y=0)



label = Label( root, text = "ADHD PREDICTION SYSTEM",font=('Elephant',24,'bold'),background="#d1b4b4")
label.place(x=200,y=5)



label_1 = Label(root, text =' Mean',font=("Helvetica", 20),background="#d1b4b4")
label_1.place(x=130,y=60)
Entry_1= Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_1.place(x=50,y=110)

label_2 = Label(root, text ='Variance',font=("Helvetica", 20),background="#d1b4b4")
label_2.place(x=110,y=140)
Entry_2 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_2.place(x=50,y=180)
        
label_3 = Label(root, text ='Standard Deviation',font=("Helvetica", 20),background="#d1b4b4")
label_3.place(x=65,y=220)
Entry_3 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_3.place(x=50,y=260)

label_4 = Label(root, text ='Entropy',font=("Helvetica", 20),background="#d1b4b4")
label_4.place(x=120,y=290)
Entry_4= Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_4.place(x=50,y=330)

label_5 = Label(root, text ='Skewness',font=("Helvetica", 18),background="#d1b4b4")
label_5.place(x=120,y=365)
Entry_5 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_5.place(x=50,y=405)

label_6 = Label(root, text ='Kurtosis',font=("Helvetica", 18),background="#d1b4b4")
label_6.place(x=120,y=440)
Entry_6 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_6.place(x=50,y=475)

label_7 = Label(root, text ='Contrast',font=("Helvetica", 18),background="#d1b4b4")
label_7.place(x=120,y=505)
Entry_7 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_7.place(x=50,y=535)

label_8 = Label(root, text ='Energy',font=("Helvetica", 18),background="#d1b4b4")
label_8.place(x=120,y=565)
Entry_8 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_8.place(x=50,y=595)

label_9 = Label(root, text ='ASM',font=("Helvetica", 18),background="#d1b4b4")
label_9.place(x=500,y=60)
Entry_9 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_9.place(x=450,y=110)

label_10 = Label(root, text ='Homogeneity',font=("Helvetica", 18),background="#d1b4b4")
label_10.place(x=500,y=140)
Entry_10 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_10.place(x=450,y=180)

label_11 = Label(root, text ='Dissimilarity',font=("Helvetica", 18),background="#d1b4b4")
label_11.place(x=500,y=220)
Entry_11 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_11.place(x=450,y=260)

label_12 = Label(root, text ='Correlation',font=("Helvetica", 18),background="#d1b4b4")
label_12.place(x=500,y=290)
Entry_12 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_12.place(x=450,y=330)

label_13 = Label(root, text ='Coarseness',font=("Helvetica", 18),background="#d1b4b4")
label_13.place(x=500,y=365)
Entry_13= Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_13.place(x=450,y=405)

label_14= Label(root, text ='PSNR',font=("Helvetica", 18),background="#d1b4b4")
label_14.place(x=500,y=440)
Entry_14 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_14.place(x=450,y=475)

label_15 = Label(root, text ='SSIM',font=("Helvetica", 18),background="#d1b4b4")
label_15.place(x=500,y=505)
Entry_15 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_15.place(x=450,y=535)

label_16 = Label(root, text ='MSE',font=("Helvetica", 18),background="#d1b4b4")
label_16.place(x=500,y=565)
Entry_16 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_16.place(x=450,y=595)

label_17 = Label(root, text ='DC',font=("Helvetica", 18),background="#d1b4b4")
label_17.place(x=800,y=60)
Entry_17 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_17.place(x=750,y=110)


def predict_rf():
    Mean =  Entry_1.get()
    Variance =  Entry_2.get()
    Standard_Deviation =  Entry_3.get()
    Entropy =  Entry_4.get()
    Skewness =  Entry_5.get()
    Kurtosis =  Entry_6.get()
    Contrast =  Entry_7.get()
    Energy =  Entry_8.get()
    ASM =  Entry_9.get()
    Homogeneity =  Entry_10.get()
    Dissimilarity =  Entry_11.get()
    Correlation =  Entry_12.get()
    Coarseness =  Entry_13.get()
    PSNR =  Entry_14.get()
    SSIM =  Entry_15.get()
    MSE =  Entry_16.get()
    DC =  Entry_17.get()

       
    out = rf.predict([[float(Mean),
       float(Variance),
       float(Standard_Deviation),
       float(Entropy),
       float(Skewness),
       float(Kurtosis),
       float(Contrast),
       float(Energy),
       float(ASM),
       float(Homogeneity),
       float(Dissimilarity),
       float(Correlation),
       float(Coarseness),
       float(PSNR),
       float(SSIM),
       float(MSE),
       float(DC)]])


    
    print(out[0])
    if out[0] == 0 :
        res_rf="NO ADHD"
        output_rf.configure(text=res_rf,font=("Helvetica", 20),fg="#1cfc08",bg="#d1b4b4")
    elif out[0] == 1: 
        res_rf="ADHD"
        output_rf.configure(text=res_rf,font=("Helvetica", 20),fg="#fc0808",bg="#d1b4b4")

def predict_dt():
    Mean =  Entry_1.get()
    Variance =  Entry_2.get()
    Standard_Deviation =  Entry_3.get()
    Entropy =  Entry_4.get()
    Skewness =  Entry_5.get()
    Kurtosis =  Entry_6.get()
    Contrast =  Entry_7.get()
    Energy =  Entry_8.get()
    ASM =  Entry_9.get()
    Homogeneity =  Entry_10.get()
    Dissimilarity =  Entry_11.get()
    Correlation =  Entry_12.get()
    Coarseness =  Entry_13.get()
    PSNR =  Entry_14.get()
    SSIM =  Entry_15.get()
    MSE =  Entry_16.get()
    DC =  Entry_17.get()

       
    out = dt.predict([[float(Mean),
       float(Variance),
       float(Standard_Deviation),
       float(Entropy),
       float(Skewness),
       float(Kurtosis),
       float(Contrast),
       float(Energy),
       float(ASM),
       float(Homogeneity),
       float(Dissimilarity),
       float(Correlation),
       float(Coarseness),
       float(PSNR),
       float(SSIM),
       float(MSE),
       float(DC)]])

    
    print(out[0])
    if out[0] == 0 :
        res_dt=" NO ADHD"
        output_dt.configure(text=res_dt,font=("Helvetica", 20),fg="#1cfc08",bg="#d1b4b4")
    elif out[0] == 1: 
        res_dt=" ADHD "
        output_dt.configure(text=res_dt,font=("Helvetica", 20),fg="#fc0808",bg="#d1b4b4")
    

     
    

b1 = Button(root, text = 'predict_dt',font=("Helvetica", 18),background="#d1b4b4",command=predict_dt)
b1.place(x=100,y=650)
    

output_dt = Label(root,background="#d1b4b4")
output_dt.place(x=250,y=650)


b1 = Button(root, text = 'predict_rf',font=("Helvetica", 18),background="#d1b4b4",command=predict_rf)
b1.place(x=400,y=650)
    

output_rf = Label(root,background="#d1b4b4")
output_rf.place(x=550,y=650)
    
root.mainloop()
