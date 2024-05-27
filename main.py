import pandas as pd
from math import *
from tkinter.scrolledtext import ScrolledText

df=pd.read_excel('Dataset/Elementopedia_Dataset.xlsx')
d=df.to_dict()

from tkinter import *
win=Tk()
win.state('zoomed')

#images
img_1=PhotoImage(file="Files/Home Page.png")
img_2=PhotoImage(file="Files/Home_Button.png")
img_3=PhotoImage(file="Files/Menu_Button.png")
img_4=PhotoImage(file="Files/Start_Button.png")
img_5=PhotoImage(file="Files/Menu.png")
ae_img=PhotoImage(file="Files/About Elementopedia.png")
c_img=PhotoImage(file="Files/Credits.png")
tc_img=PhotoImage(file="Files/T&C.png")
h_img=PhotoImage(file="Files/Help.png")
kate_b_img=PhotoImage(file="Files/KATE.png")
soe_b_img=PhotoImage(file="Files/SOE.png")
iec_b_img=PhotoImage(file="Files/IEC.png")
sctc_b_img=PhotoImage(file="Files/SCTC.png")
kate_bg_img=PhotoImage(file="Files/KATE_pg.png")
show_button=PhotoImage(file="Files/show_button.png")
soe_bg_img=PhotoImage(file="Files/soe_bg_img.png")
soe_bg_img2=PhotoImage(file="Files/soe_bg_img2.png")
iec_bg_img=PhotoImage(file="Files/iec_bg_img.png")
kate_print=PhotoImage(file="Files/kate_display_print.png")
back=PhotoImage(file="Files/back_button.png")
iec_output_pg=PhotoImage(file="Files/iec_output_bg.png")
sctc_bg_img=PhotoImage(file="Files/sctc_bg_img.png")
proceed_button=PhotoImage(file="Files/proceed_button.png")
sctc_bg2=PhotoImage(file="Files/sctc_output_bg.png")

#home page
def home_pg():
    win.title('Elementopedia - Home')
    home_frame=Frame(win,height=700,width=1400).place(x=0,y=0)
    home_bg=Label(home_frame,image=img_1).place(x=0,y=0)
    
    def abt_popup():
        win2=Tk()
        win2.title('About Elementopedia')
        win2.geometry('1000x550')
        win2.resizable(False,False)

        f=open('Files/abt.txt')
        abt=f.read()

        a=ScrolledText(win2,width=900,font=('Century Gothic',15))
        a.grid(row=0,column=0)
        a.insert(INSERT,abt)
        a.configure(state=DISABLED)
        
    def cdt_popup():
        win3=Tk()
        win3.title('Credits')
        win3.geometry('1000x550')
        win3.resizable(False,False)

        f=open('Files/cdt.txt')
        abt=f.read()

        a=ScrolledText(win3,width=900,font=('Century Gothic',15))
        a.grid(row=0,column=0)
        a.insert(INSERT,abt)
        a.configure(state=DISABLED)

    def tnc_popup():
        win4=Tk()
        win4.title('Terms and Conditions')
        win4.geometry('1000x550')
        win4.resizable(False,False)

        f=open('Files/tnc.txt')
        abt=f.read()

        a=ScrolledText(win4,width=900,font=('Century Gothic',15))
        a.grid(row=0,column=0)
        a.insert(INSERT,abt)
        a.configure(state=DISABLED)

    def hlp_popup():
        win5=Tk()
        win5.title('Help')
        win5.geometry('1000x575')
        win5.resizable(False,False)

        f=open('Files/hlp.txt')
        abt=f.read()

        a=ScrolledText(win5,width=900,font=('Century Gothic',15))
        a.grid(row=0,column=0)
        a.insert(INSERT,abt)
        a.configure(state=DISABLED)
    

    start_button=Button(home_frame,image=img_4,command=menu_pg).place(x=550,y=375)
    ae_button=Button(home_frame,image=ae_img,command=abt_popup).place(x=125,y=620)
    c_button=Button(home_frame,image=c_img,command=cdt_popup).place(x=425,y=620)
    tc_button=Button(home_frame,image=tc_img,command=tnc_popup).place(x=725,y=620)
    h_button=Button(home_frame,image=h_img,command=hlp_popup).place(x=1025,y=620)

#menu page
def menu_pg():
    win.title('Elementopedia - Home > Menu')
    menu_frame=Frame(win,height=700,width=1400).place(x=0,y=0)
    menu_bg=Label(menu_frame,image=img_5).place(x=0,y=0)
    home_button=Button(menu_frame,image=img_2,command=home_pg).place(x=2,y=0)
    kate_button=Button(menu_frame,image=kate_b_img,command=kate_pg).place(x=100,y=350)
    soe_button=Button(menu_frame,image=soe_b_img,command=soe_pg).place(x=700,y=350)
    iec_button=Button(menu_frame,image=iec_b_img,command=iec_pg).place(x=100,y=475)
    sctc_button=Button(menu_frame,image=sctc_b_img,command=sctc_pg).place(x=100,y=600)

#know about the element
def kate_pg():
    win.title('Elementopedia - Home > Know about the Element')
    kate_frame=Frame(win,height=700,width=1400).place(x=0,y=0)
    kate_bg=Label(kate_frame,image=kate_bg_img).place(x=-20,y=0)
    home_button=Button(kate_frame,image=img_2,command=home_pg).place(x=2,y=0)
    menu_button=Button(kate_frame,image=img_3,command=menu_pg).place(x=1230,y=0)
    entry_kate=Entry(kate_frame,background='grey',font=('century gothic',45,'normal'))
    entry_kate.place(x=255,y=375,width=850,height=100)
    
    def kate_disp():
        e_name=entry_kate.get()
        
        if e_name.isnumeric():
            e_name=int(e_name)
        if e_name in d:
            e_name_=d[e_name][1]
            kate_output(e_name_,d[e_name])
        else:
            win6=Tk()
            win6.title('Element not found')
            win6.resizable(False,False)
            err=Label(win6,text='Element not found!! Retry again and click Show',font=('Century gothic',25),fg='black').pack()
    show=Button(kate_frame,image=show_button,command=kate_disp).place(x=220,y=490)
    
def kate_output(e_name_,element):
    win.title('Elementopedia - Home > Know about the Element > Element Details')
    kate_output_frame=Frame(win,height=700,width=1400).place(x=0,y=0)
    kate_output_bg=Label(kate_output_frame,image=kate_print).place(x=-20,y=0)
    back_button=Button(kate_output_frame,image=back,command=kate_pg).place(x=1230,y=0)
    e_disp=Label(kate_output_frame,text=e_name_,font=('times new roman',60,'normal'),bg='#e8b862').place(x=700,y=20)
    symbol=Label(kate_output_frame,text=element[0],font=('Century gothic',35),bg='#d9d9d9').place(x=400,y=143)
    atm_no=Label(kate_output_frame,text=element[2],font=('Century gothic',35),bg='#d9d9d9').place(x=400,y=227)
    mass=Label(kate_output_frame,text=element[3],font=('Century gothic',35),bg='#d9d9d9').place(x=400,y=305)
    e=str(element[4])+' , '+str(element[5])
    grp=Label(kate_output_frame,text=e,font=('Century gothic',35),bg='#d9d9d9').place(x=400,y=385)
    blk=Label(kate_output_frame,text=element[6],font=('Century gothic',35),bg='#d9d9d9').place(x=400,y=465)
    econ=element[7]
    res_econ=''
    e={0:'\u00b0',1:'\u00b9',2:'\u00b2',3:'\u00b3',4:'\u2074',5:'\u2075',6:'\u2076',7:'\u2077',8:'\u2078',9:'\u2079',}
    i=0
    while i < len(econ):
        if econ[i] in 'spdf':
            if (i+2)<len(econ):
                if econ[i+2].isspace():
                    res_econ+=econ[i]+e[int(econ[i+1])]
                    i+=2
                elif (econ[i+2]).isdigit():
                    res_econ+=econ[i]+e[int(econ[i+1])]+e[int(econ[i+2])]
                    i+=3
            else:
                res_econ+=econ[i]+e[int(econ[i+1])]
                i+=2
        else:
            res_econ+=econ[i]
            i+=1
    
    econfig=Label(kate_output_frame,text=res_econ,font=('Century gothic',35),bg='#d9d9d9').place(x=550,y=545)
    if 'Solid' in element[8]:
        ele='Solid'
    elif 'Liquid' in element[8]:
        ele='Liquid'
    elif 'Gas' in element[8]:
        ele='Gas'
    std=Label(kate_output_frame,text=ele,font=('Century gothic',35),bg='#d9d9d9').place(x=400,y=625)
    if element[9]!=0:
        mel=Label(kate_output_frame,text=element[9],font=('Century gothic',35),bg='#d9d9d9').place(x=1215,y=143)
    else:
        mel=Label(kate_output_frame,text='None',font=('Century gothic',35),bg='#d9d9d9').place(x=1215,y=143)

    if element[10]!=0:
        bol=Label(kate_output_frame,text=element[10],font=('Century gothic',35),bg='#d9d9d9').place(x=1215,y=227)
    else:
        bol=Label(kate_output_frame,text='None',font=('Century gothic',35),bg='#d9d9d9').place(x=1215,y=227)

    if element[11]!=0:
        atr=Label(kate_output_frame,text=element[11],font=('Century gothic',35),bg='#d9d9d9').place(x=1215,y=305)
    else:
        atr=Label(kate_output_frame,text='None',font=('Century gothic',35),bg='#d9d9d9').place(x=1215,y=305)

    if element[12]!=0:
        en=Label(kate_output_frame,text=element[12],font=('Century gothic',35),bg='#d9d9d9').place(x=1215,y=385)
    else:
        en=Label(kate_output_frame,text='None',font=('Century gothic',35),bg='#d9d9d9').place(x=1215,y=385)

    if element[13]!=0:
        ie=Label(kate_output_frame,text=element[13],font=('Century gothic',35),bg='#d9d9d9').place(x=1215,y=465)
    else:
        ie=Label(kate_output_frame,text='None',font=('Century gothic',35),bg='#d9d9d9').place(x=1215,y=465)

    if element[14]!=0:
        ea=Label(kate_output_frame,text=element[14],font=('Century gothic',35),bg='#d9d9d9').place(x=1215,y=625)
    else:
        ea=Label(kate_output_frame,text='None',font=('Century gothic',35),bg='#d9d9d9').place(x=1215,y=625)

#sorting of elements
def soe_pg():
    
    win.title('Elementopedia - Home > Sorting of Elements')
    soe_frame=Frame(win,height=700,width=1400).place(x=0,y=0)
    soe_bg=Label(soe_frame,image=soe_bg_img).place(x=-20,y=0)
    home_button=Button(soe_frame,image=img_2,command=home_pg).place(x=2,y=0)
    menu_button=Button(soe_frame,image=img_3,command=menu_pg).place(x=1230,y=0)

    #checkboxes
    def isChecked():
        if radio.get()>=1 and radio2.get()>=1:
            show.config(state=NORMAL)
            
    radio=IntVar()
    
    chk_a=Radiobutton(soe_frame,text='Atomic Radius',font=('Century gothic', 30, 'normal'),\
                      fg='purple',bg='white',variable=radio,value=1,command=isChecked)
    chk_a.place(x=450,y=235)

    chk_e=Radiobutton(soe_frame,text='Electronegativity',font=('Century gothic', 30, 'normal'),\
                      fg='purple',bg='white',variable=radio,value=2,command=isChecked)
    chk_e.place(x=850,y=235)

    chk_i=Radiobutton(soe_frame,text='Ionization Energy',font=('Century gothic', 30, 'normal'),\
                      fg='purple',bg='white',variable=radio,value=3,command=isChecked)
    chk_i.place(x=450,y=300)

    chk_ea=Radiobutton(soe_frame,text='Electron Affinity',font=('Century gothic', 30, 'normal'),\
                       fg='purple',bg='white',variable=radio,value=4,command=isChecked)
    chk_ea.place(x=850,y=300)

    radio2=IntVar()
    chk_as=Radiobutton(soe_frame,text='Ascending order',font=('Century gothic', 30, 'normal'),\
                       fg='maroon',bg='white',variable=radio2,value=1,command=isChecked)
    chk_as.place(x=450,y=385)

    chk_ds=Radiobutton(soe_frame,text='Descending Order',font=('Century gothic', 30, 'normal'),\
                       fg='maroon',bg='white',variable=radio2,value=2,command=isChecked)
    chk_ds.place(x=850,y=385)

    
    entry_soe=Entry(soe_frame,background='grey',font=('century gothic',45,'normal'))
    entry_soe.place(x=50,y=545,width=1265,height=70)

    def soe():
        e_soe=entry_soe.get()
        e_soe=e_soe.split()
        r1=radio.get()
        r2=radio2.get()
        if len(e_soe)<=1:
            top= Toplevel(win)
            top.resizable(False,False)
            top.title("Invalid entry in Sorting of Elements")
            if len(e_soe)==0:
               Label(top,text='No Element has been entered',font=('Century gothic',25),bg='black',fg='white').pack()
            else:
                Label(top,text='Only one Element has been entered. Hence there is nothing to sort',\
                      font=('Century gothic',25),bg='black',fg='white').pack()
        else:
           soe_output(r1,r2,e_soe)

    show=Button(soe_frame,image=show_button,state=DISABLED,command=soe)
    show.place(x=220,y=615)

def soe_output(pt,o,l):
    trend,res=[],[];na=[];p=''
    pt+=10
    for i in l:
        if i in d:
            trend.append(d[i][pt])
        else:
            na.append(i)
            l.remove(i)
    if o==1:
        trend.sort()
    else:
        trend.sort(reverse=True)
    for i in trend:
        for j in l:
            if i==d[j][pt]:
                res.append(j)
            
    del trend
    del pt
    l.clear()
    for i in res:
        if i not in l:
            l.append(i)
    res=l
    del l
    if o==1:
        p=(' < '.join(res))
    else:
        p=(' > '.join(res))

    if na==[]:
        na='None'
    else:
        na=' , '.join(na)
    win.title('Elementopedia - Home > Sorting of Elements > Sorted Elements')
    soe_output_frame=Frame(win,height=700,width=1400).place(x=0,y=0)
    soe_output_bg=Label(soe_output_frame,image=soe_bg_img2).place(x=-20,y=0)
    back_button=Button(soe_output_frame,image=back,command=soe_pg).place(x=1230,y=0)

    Label(soe_output_frame,text=p,font=('Century Gothic', 40),bg='white').place(x=75,y=250)

    Label(soe_output_frame,text='Elements not identified - > ',font=('Century Gothic', 35),\
          bg='black',fg='white').place(x=75,y=500)
    Label(soe_output_frame,text=na,font=('Century Gothic', 35),bg='white').place(x=750,y=500)
    
#Identification of Elements in a Compound
def iec_pg():
    win.title('Elementopedia - Home > Identification of Elements in a Compound')
    iec_frame=Frame(win,height=700,width=1400).place(x=0,y=0)
    iec_bg=Label(iec_frame,image=iec_bg_img).place(x=-20,y=0)
    home_button=Button(iec_frame,image=img_2,command=home_pg).place(x=2,y=0)
    menu_button=Button(iec_frame,image=img_3,command=menu_pg).place(x=1230,y=0)
    entry_iec=Entry(iec_frame,background='grey',font=('century gothic',45,'normal'))
    entry_iec.place(x=240,y=450,width=880,height=100)

    def pass_iec():
        compound=entry_iec.get()
        if compound=='':
            top= Toplevel(win)
            top.resizable(False,False)
            top.title("Invalid entry in Identification of Elements in a Compound")
            Label(top,text='No Compound has been entered',font=('Century gothic',25),bg='black',fg='white').pack()
        else:
            iec_output(compound)

    show=Button(iec_frame,image=show_button,command=pass_iec).place(x=220,y=550)

def iec_output(compound):
    
    s=compound.strip()+" "
    i,r,l=0,'',[]
    while i<len(s):
        if s[i].isalpha():
            r=s[i]
            if s[i+1].islower():
                r+=s[i+1]
                i+=2
            else:
                i+=1
            if r not in l:
                l.append(r)
                r=""
        else:
            i+=1
    d_iec={};nf=[]
    for i in l:
        if i not in d.keys():
            nf.append(i)
    
        else:
            d_iec[i]=d[i][1]

    iec_output_frame=Frame(win,height=700,width=1400).place(x=0,y=0)
    iec_out_bg=Label(iec_output_frame,image=iec_output_pg).place(x=-20,y=0)
    home_button=Button(iec_output_frame,image=img_2,command=home_pg).place(x=2,y=0)
    back_button=Button(iec_output_frame,image=back,command=iec_pg).place(x=1230,y=0)
    k=list(d_iec.keys())
    x_,y_=75,250
    for i in range(len(k)):
        t=k[i]+' -> '+d_iec[k[i]]
        if i%3 == 0 and i!=0:
            y_+=75
            x_=75
        elif i!=0:
            x_+=400
        lb=Label(iec_output_frame,text=t,font=('Century Gothic', 35),bg='white').place(x=x_,y=y_)
    Label(iec_output_frame,text='Elements not identified - > ',font=('Century Gothic', 35),\
          bg='black',fg='white').place(x=75,y=y_+100)
    x_=500
    if nf==[]:
        Label(iec_output_frame,text='None',font=('Century Gothic', 35),bg='white').place(x=x_+200,y=y_+100)
    else:
        for i in nf:
            lb=Label(iec_output_frame,text=i,font=('Century Gothic', 35),bg='white').place(x=x_+200,y=y_+100)
            x_+=200

#stoichiometric concentration terms converter
def sctc_pg():
    win.title('Elementopedia - Home > Stoichiometric Concentration Terms Converter')
    sctc_frame=Frame(win,height=700,width=1400).place(x=0,y=0)
    sctc_bg=Label(sctc_frame,image=sctc_bg_img).place(x=-20,y=0)
    home_button=Button(sctc_frame,image=img_2,command=home_pg).place(x=2,y=0)
    menu_button=Button(sctc_frame,image=img_3,command=menu_pg).place(x=1230,y=0)

    def isChecked():
        pass
            
    radio=IntVar()
    
    Mm=Radiobutton(sctc_frame,text='Molarity to Molality',font=('Century gothic', 30, 'normal'),\
                      fg='red',bg='white',variable=radio,value=1)
    Mm.place(x=200,y=275)

    mM=Radiobutton(sctc_frame,text='Molality to Molarity',font=('Century gothic', 30, 'normal'),\
                      fg='purple',bg='white',variable=radio,value=2)
    mM.place(x=675,y=275)

    MN=Radiobutton(sctc_frame,text='Molarity to Normality',font=('Century gothic', 30, 'normal'),\
                      fg='green',bg='white',variable=radio,value=3)
    MN.place(x=200,y=375)

    NM=Radiobutton(sctc_frame,text='Normality to Molarity',font=('Century gothic', 30, 'normal'),\
                      fg='blue',bg='white',variable=radio,value=4)
    NM.place(x=675,y=375)

    mN=Radiobutton(sctc_frame,text='Molality to Normality',font=('Century gothic', 30, 'normal'),\
                      fg='black',bg='white',variable=radio,value=5)
    mN.place(x=200,y=475)

    Nm=Radiobutton(sctc_frame,text='Normality to Molality',font=('Century gothic', 30, 'normal'),\
                      fg='maroon',bg='white',variable=radio,value=6)
    Nm.place(x=675,y=475)

    def sctc_output():
        r=radio.get()
        if r>=1:
            sctc_output_pg(r)
        else:
            top= Toplevel(win)
            top.resizable(False,False)
            top.title("Invalid entry in Stoichiometric Concentration Terms Converter")
            Label(top,text='No conversion has been selected',font=('Century gothic',25),bg='black',fg='white').pack()

    proceed=Button(sctc_frame,image=proceed_button,command=sctc_output).place(x=225,y=550)

def sctc_output_pg(r):

    sctc_output_frame=Frame(win,height=700,width=1400).place(x=0,y=0)
    sctc_bg_new=Label(sctc_output_frame,image=sctc_bg2).place(x=-20,y=0)
    home_button=Button(sctc_output_frame,image=img_2,command=home_pg).place(x=2,y=0)
    back_button=Button(sctc_output_frame,image=back,command=sctc_pg).place(x=1230,y=0)

    c1=Label(sctc_output_frame,font=('century gothic',30,'bold'),bg='white')
    c2=Label(sctc_output_frame,font=('century gothic',30,'bold'),bg='white')
    c3=Label(sctc_output_frame,font=('century gothic',30,'bold'),bg='white')
    c4=Label(sctc_output_frame,font=('century gothic',30,'bold'),bg='white')
    result_label=Label(sctc_output_frame,font=('century gothic',30,'bold'),bg='black',fg='white')
    
    e1=Entry(sctc_output_frame,background='grey',font=('century gothic',30,'normal'))
    e2=Entry(sctc_output_frame,background='grey',font=('century gothic',30,'normal'))
    e3=Entry(sctc_output_frame,background='grey',font=('century gothic',30,'normal'))
    e4=Entry(sctc_output_frame,background='grey',font=('century gothic',30,'normal'))

    calc=Button(sctc_output_frame,text='CALCULATE',bg='orange',fg='black',\
                font=('century gothic',30,'normal'))

    if r==1:

        c1.config(text="Concentration (in Molar - mol/litre)")
        c1.place(x=150,y=250)
        e1.place(x=925,y=250,width=300,height=60)
        c2.config(text="Density of solvent (in kg/litre)")
        c2.place(x=150,y=325)
        e2.place(x=925,y=325,width=300,height=60)
        c3.config(text="Molar Mass of solute (in gm)")
        c3.place(x=150,y=400)
        e3.place(x=925,y=400,width=300,height=60)

        def result_def():
            cns=e1.get();ps=e2.get();Ms=e3.get()
            if cns=='' or ps=='' or Ms=='':
                top=Toplevel(win)
                top.resizable(False,False)
                top.title('Blank entry in Stoichiometric Conc. Terms Converter')
                Label(top,text='Blank Entry!!! Please provide a valid entry').pack()
            else:
                cn=float(cns)
                p=float(ps)
                M=(float(Ms))
                result=(cn)/(((p)-(M/1000)))
                #result=round(result,12)
                result=str(result)[:14]
                res=Label(sctc_output_frame,font=('century gothic',30,'bold'),bg='grey',fg='black')
                res.config(text=result)
                res.place(x=925,y=600)
        
        calc.place(x=150,y=550,width=1082,height=50)
        calc.config(command=result_def)
       
        result_label.config(text='Molality (in molal - mol/kg)\t\t\t  ')
        result_label.place(x=150,y=600)

    if r==2:
        
        c1.config(text="Concentration (in molal - mol/kg)")
        c1.place(x=150,y=250)
        e1.place(x=925,y=250,width=300,height=60)
        c2.config(text="Density (in kg/litre)")
        c2.place(x=150,y=325)
        e2.place(x=925,y=325,width=300,height=60)
        c3.config(text="Molecular weight of solute (in gm)")
        c3.place(x=150,y=400)
        e3.place(x=925,y=400,width=300,height=60)

        def result_def():
            cns=e1.get();ps=e2.get();Ms=e3.get()
            if cns=='' or ps=='' or Ms=='':
                top=Toplevel(win)
                top.resizable(False,False)
                top.title('Blank entry in Stoichiometric Conc. Terms Converter')
                Label(top,text='Blank Entry!!! Please provide a valid entry').pack()
            else:
                cns=float(cns)
                ps=float(ps)
                Ms=(float(Ms))
                result= cns*(ps-(Ms/1000))
                result=str(result)[:14]
                res=Label(sctc_output_frame,font=('century gothic',30,'bold'),bg='grey',fg='black')
                res.config(text=result)
                res.place(x=925,y=600)
        
        calc.place(x=150,y=550,width=1082,height=50)
        calc.configure(command=result_def)
    
        result_label.config(text='Molarity (in Molar - mol/litre)\t\t\t  ')
        result_label.place(x=150,y=600)

    if r==3:

        c1.config(text="Concentration (in Molar - mol/litre)")
        c1.place(x=150,y=250)
        e1.place(x=925,y=250,width=300,height=60)
        c2.config(text="Valency factor")
        c2.place(x=150,y=325)
        e2.place(x=925,y=325,width=300,height=60)

        def result_def():
            cns=e1.get();xs=e2.get()
            if cns=='' or xs=='':
                top=Toplevel(win)
                top.resizable(False,False)
                top.title('Blank entry in Stoichiometric Conc. Terms Converter')
                Label(top,text='Blank Entry!!! Please provide a valid entry').pack()
            else:
                cn=float(cns)
                x=float(xs)
                result= (cn*x)
                result=str(result)[:14]
                res=Label(sctc_output_frame,font=('century gothic',30,'bold'),bg='grey',fg='black')
                res.config(text=result)
                res.place(x=925,y=600)
        
        calc.place(x=150,y=550,width=1082,height=50)
        calc.configure(command=result_def)

        
        result_label.config(text='Normality (in Normal)\t\t\t\t  ')
        result_label.place(x=150,y=600)

    if r==4:
        c1.config(text="Concentration (in Normal)")
        c1.place(x=150,y=250)
        e1.place(x=925,y=250,width=300,height=60)
        c2.config(text="Valency factor")
        c2.place(x=150,y=325)
        e2.place(x=925,y=325,width=300,height=60)
        
        def result_def():
            cns=e1.get();xs=e2.get()
            if cns=='' or xs=='':
                top=Toplevel(win)
                top.resizable(False,False)
                top.title('Blank entry in Stoichiometric Conc. Terms Converter')
                Label(top,text='Blank Entry!!! Please provide a valid entry').pack()
            else:
                cn=float(cns)
                x=float(xs)
                result= (cn/x)
                result=str(result)[:14]
                res=Label(sctc_output_frame,font=('century gothic',30,'bold'),bg='grey',fg='black')
                res.config(text=result)
                res.place(x=925,y=600)

        calc.place(x=150,y=550,width=1082,height=50)
        calc.configure(command=result_def)
        
        result_label.config(text='Molarity (in Molar - mol/litre)\t\t\t  ')
        result_label.place(x=150,y=600)

    if r==5:
        
        c1.config(text="Concentration (in molal - mol/kg)")
        c1.place(x=150,y=250)
        e1.place(x=925,y=250,width=300,height=60)
        c2.config(text="Density (in kg/litre)")
        c2.place(x=150,y=325)
        e2.place(x=925,y=325,width=300,height=60)
        c3.config(text="Molecular weight of solute (in gm)")
        c3.place(x=150,y=400)
        e3.place(x=925,y=400,width=300,height=60)
        c4.config(text="Valency factor")
        c4.place(x=150,y=475)
        e4.place(x=925,y=475,width=300,height=60)

        def result_def():
            cns=e1.get();ps=e2.get();Ms=e3.get();xs=e4.get()
            if cns=='' or ps=='' or Ms=='' or xs=='':
                top=Toplevel(win)
                top.resizable(False,False)
                top.title('Blank entry in Stoichiometric Conc. Terms Converter')
                Label(top,text='Blank Entry!!! Please provide a valid entry').pack()
            else:
                cn=float(cns)
                p=float(ps)
                M=(float(Ms))
                result= (cn)*(((p)-(M/1000)))
                result=result*float(xs)
                result=str(result)[:14]
                res=Label(sctc_output_frame,font=('century gothic',30,'bold'),bg='grey',fg='black')
                res.config(text=result)
                res.place(x=925,y=600)
        
        calc.place(x=150,y=550,width=1082,height=50)
        calc.configure(command=result_def)
        
        result_label.config(text='Normality (in Normal)\t\t\t\t  ')
        result_label.place(x=150,y=600)

    if r==6:
        
        c1.config(text="Concentration (in Normal)")
        c1.place(x=150,y=250)
        e1.place(x=925,y=250,width=300,height=60)
        c2.config(text="Density (in kg/litre)")
        c2.place(x=150,y=325)
        e2.place(x=925,y=325,width=300,height=60)
        c3.config(text="Molecular weight of solute (in gm)")
        c3.place(x=150,y=400)
        e3.place(x=925,y=400,width=300,height=60)
        c4.config(text="Valency factor")
        c4.place(x=150,y=475)
        e4.place(x=925,y=475,width=300,height=60)

        def result_def():
            cns=e1.get();ps=e2.get();Ms=e3.get();xs=e4.get()
            if cns=='' or ps=='' or Ms=='' or xs=='':
                top=Toplevel(win)
                top.resizable(False,False)
                top.title('Blank entry in Stoichiometric Conc. Terms Converter')
                Label(top,text='Blank Entry!!! Please provide a valid entry').pack()
            else:
                cns=float(cns)
                xs=float(xs)
                cns= (cns/xs)
                #cn=cn*1000
                p=float(ps)
                M=(float(Ms))
                result=(cns)/(((p)-(M/1000)))
                result=str(result)[:14]
                res=Label(sctc_output_frame,font=('century gothic',30,'bold'),bg='grey',fg='black')
                res.config(text=result)
                res.place(x=925,y=600)

        calc.place(x=150,y=550,width=1082,height=50)
        calc.configure(command=result_def)
     
        result_label.config(text='Molality (in molal - mol/kg)\t\t\t  ')
        result_label.place(x=150,y=600)
    
home_pg()

win.mainloop()
