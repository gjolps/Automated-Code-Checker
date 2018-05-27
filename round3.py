from tkinter import *
from subprocess import Popen
from subprocess import PIPE
import os
import random


global flag,qt,path
path = str(os.getcwd()) + "/TestCases"
flag = 0
qt = 0
class App:

    editor = NONE
    case_count = 0
    counter = 0
    display_message = NONE
    c_btn = NONE
    cpp_btn = NONE
    lang = NONE

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.gui(frame)


    def gui(self,frame):

        welcome = Label(frame,text="ROUND 3",fg="blue")
        welcome.grid(row=0, column=0,sticky=N)

        global qt
        qt = 1
        q_file = open((str(qt)+".txt"),'r')
        #q_file = open("1.txt",'r')
        question = q_file.read()
        q1 = Message(frame,text=question,bd=14,aspect=700,bg="yellow",fg="red")
        q1.grid(row=1,sticky=W)

        global cpp_btn,c_btn,lang
        lang = IntVar()
        lang.set(1)
        c_btn = Radiobutton(frame,text="C Language",fg='green',variable='lang',value=0,command=self.set_c)
        c_btn.grid(row=2,sticky=N)
        cpp_btn = Radiobutton(frame,text="C++ Language",fg='green',variable='lang',value=1,command=self.set_cpp)
        cpp_btn.grid(row=3,sticky=N)


        global editor
        editor = Text(frame,height=20,width=175)
        editor.grid(row=4,sticky=W)
        editor.insert(END,"//Enter your code here..")


        Button(frame,text="COMPILE",command=self.run_file).grid(row=5, column=0)
        Button(frame,text="SUBMIT",command=self.submit).grid(row=6, column=0)

        global display_message
        display_message = Text(frame,height=10,width=175)
        display_message.grid(row=7,sticky=W)



    def set_c(self):
        global lang
        lang.set(0)
    def set_cpp(self):
        global lang
        lang.set(1)


    def run_file(self):
        global c_btn,cpp_btn,lang
        global display_message
        global editor

        if lang.get()==0:
            #print(lang.get())
            self.compile_pgm(1)
        else:
            #print(lang.get())
            self.compile_pgm(2)


    def submit(self):
        global display_message
        if not os.path.isfile("./a.out"):
            display_message.delete('1.0', END)
            display_message.insert(END,"Please Compile your Code first\n")


        else:
            global qt,path
            if os.path.isfile("tmp.txt"):
                tmp_file = open("tmp.txt",'w')
            else:
                tmp_file = open("tmp.txt",'a')

            #"/home/codemiester/PycharmProjects/C-Wiz/Round2/TestCases/input_"+str(qt)+".txt",'rb'
            with open(path+"/input_"+str(qt)+".txt",'rb') as input_file:
                for i in input_file:
                    #print("Feeding {} to program".format(i.decode("ascii").strip()))
                    proc = Popen("./a.out", stdin=PIPE, stdout=PIPE, stderr=PIPE)
                    out,err = proc.communicate(input=i)
                    if len(str(err))>3:
                        display_message.insert('1.0',"\n"+str(err).split("b")[1].split("'")[1] + "\n")
                    tmp_file.write(str(out).split("b")[1].split("'")[1] + "\n")
            tmp_file.close()

            tmp_file = open("tmp.txt",'r')
            out_file = open(path+"/output_"+str(qt)+".txt",'r')
            #out_file = open("/home/codemiester/PycharmProjects/C-Wiz/Round3/TestCases/output_2.txt",'r')
            t = tmp_file.readlines()
            o = out_file.readlines()

            test_count = 0

            display_message.insert('1.0',"Result : \n")
            for i in range(len(t)):
                display_message.insert(END,"Your Output : "+t[i])

            for i in range(len(t)):
                display_message.insert(END,"Your Output : "+t[i])
                if t[i]==o[i]:
                    test_count+=1
                    display_message.insert(END,"Test Case "+str(i)+" Pass\n\n")
                else:
                    display_message.insert(END,"Test Case "+str(i)+" Fail\n")
            display_message.insert(END,"Total : "+str(test_count)+"/"+str(len(t))+" Passed")

            tmp_file.close()
            out_file.close()
            if test_count==len(t):
                global flag
                flag = 1
                #print("Success!!!")



    def compile_pgm(self,val):
        global display_message
        if val==1:
            display_message.delete('1.0', END)
            display_message.insert('1.0',"Opening File 1.c...\n")
            file = open("1.c",'w')
            file.write(editor.get('1.0','end-1c'))
            display_message.insert(END,"Finished writing contents in to the File....\nClosing File... \n")
            file.close()
            display_message.insert(END,"Compiling file... \n")
            proc = Popen(["gcc","1.c"],stdout=PIPE,stderr=PIPE)
            out, err = proc.communicate()
            if(len(err)>0):
                err_msg = "Error Message :- \n\t"+str(err).replace("b","",1)+"\n"
                err_msg = err_msg.replace("\\xe2\\x80\\x98","'")
                err_msg = err_msg.replace("\\xe2\\x80\\x99","'")
                display_message.insert('1.0',err_msg)
            else:
                display_message.insert(END,"Program Successfully Compiled...\n")

        else:
            display_message.delete('1.0', END)
            display_message.insert('1.0',"Opening File 1.cpp...\n")
            file = open("1.cpp",'w')
            file.write(editor.get('1.0','end-1c'))
            display_message.insert(END,"Finished writing contents in to the File....\nClosing File... \n")
            file.close()
            display_message.insert(END,"Compiling file... \n")
            proc = Popen(["g++","1.cpp"],stdout=PIPE,stderr=PIPE)
            out, err = proc.communicate()
            if(len(err)>0):
                err_msg = "Error Message :- \n\t"+str(err).replace("b","",1)+"\n"
                err_msg = err_msg.replace("\\xe2\\x80\\x98","'")
                err_msg = err_msg.replace("\\xe2\\x80\\x99","'")
                display_message.insert(END,err_msg)
            else:
                display_message.insert(END,"Program Successfully Compiled...\n")


class Counter:

    timer = 0

    def __init__(self,master):
        frame = Frame(master)

        frame.pack()

        msg = Label(frame,fg="white",font=(None,20),bg="black",height=10,width=10)
        msg.pack()

        self.timer(msg)

    def do_nothing(self):
        pass

    def timer(self,msg):
        global timer
        timer = 0
        def count():
            global flag
            if(flag==0):
                global timer
                timer += 1
                minutes = timer//60
                seconds = timer%60
                time = str(minutes)+":"+str(seconds)
                msg.config(text=time)
                msg.after(1000,count)
                msg.pack(side=LEFT)
            else:
                print("\nCongratulations!!! All Test Cases have passed Successfully\nTotal Time Taken : ",self.get_time())
        count()

    def get_time(self):
        global timer
        return (str(timer//60)+":"+str(timer%60))



root = Tk()
root.title("C-WIZ")
root1 = Tk()
root1.title("Timer")
app = App(root)

time = Counter(root1)
root.mainloop()
root1.mainloop()
