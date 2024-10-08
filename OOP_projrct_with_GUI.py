from tkinter import *
from mydb import Database
from tkinter import messagebox
import nlpcloud

class NLPApp:
    def __init__(self):

        # create db object
        self.ob = Database()

        # login gui loads
        self.root = Tk()
        self.root.title('NLPApp')

        self.root.geometry('350x600')
        self.root.configure(bg='#616a6b')
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):

        self.clear()
        
        heading = Label(self.root,text='NLPApp', bg='#616a6b', fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))
        label1 = Label(self.root,text="Enter Email")
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5,10), ipady=4)
        
        label2 = Label(self.root,text="Enter Password")
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root, width=30, show='*')
        self.password_input.pack(pady=(5,10), ipady=4)
        
        login_btn = Button(self.root, text='Login', width=30,height=2, command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root,text="Not a member?")
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root, text='Register Now', command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root,text='NLPApp', bg='#616a6b', fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))
        
        label0 = Label(self.root,text="Enter Name")
        label0.pack(pady=(10,10))

        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(5,10), ipady=4)

        label1 = Label(self.root,text="Enter Email")
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5,10), ipady=4)
        
        label2 = Label(self.root,text="Enter Password")
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root, width=30,show='*')
        self.password_input.pack(pady=(5,10), ipady=4)
        
        register_btn = Button(self.root, text='Register', width=30,height=2, command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        label3 = Label(self.root,text="Already a member?")
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root, text='Register Now', command=self.login_gui)
        redirect_btn.pack(pady=(10,10))

    def clear(self):
        # clear the gui
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        # fetch data from gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.ob.add_data(name,email,password)
        if response:
            messagebox.showinfo('Success','Registration successful')
        else:
            messagebox.showerror('Email Already exist')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.ob.search(email,password)

        if response:
            messagebox.showinfo('Success', 'Login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect email/password')

    def home_gui(self):
        self.clear()

        heading = Label(self.root,text='NLPApp', bg='#616a6b', fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30,height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30,height=4, command=self.ner_gui)
        ner_btn.pack(pady=(10,10))

        emotion_btn = Button(self.root, text='Summerization', width=30,height=4, command=self.emotion_gui)
        emotion_btn.pack(pady=(10,10))


        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack(pady=(10,10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root,text='NLPApp', bg='#616a6b', fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root,text='Sentiment Analysis', bg='#616a6b', fg='white')
        heading2.pack(pady=(10,20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root,text="Enter the text")
        label1.pack(pady=(10,10))
        
        self.sentiment_input = Entry(self.root, width=30)
        self.sentiment_input.pack(pady=(5,10), ipady=4)
        
        sentiment_btn = Button(self.root, text='Analyze Sentiment', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))
        
        self.sentiment_result = Label(self.root,text="",bg='#616a6b' ,fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana',16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10,10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        
        client = nlpcloud.Client("distilbert-base-uncased-emotion", "2b21ce3bf88d4ba196c69b7c42119a9cc8c33766", gpu=False)
        response = client.sentiment(text)

        L = []
        for i in response['scored_labels']:
            L.append(i['score'])

        index = sorted(list(enumerate(L)), key= lambda x:x[1], reverse=True)[0][0]

        new_res = response['scored_labels'][index]['label']
        self.sentiment_result['text'] = new_res

    

    def ner_gui(self):
        self.clear()

        heading = Label(self.root,text='NLPApp', bg='#616a6b', fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root,text='NER', bg='#616a6b', fg='white')
        heading2.pack(pady=(10,20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root,text="Enter the text")
        label1.pack(pady=(10,10))
        
        self.ner_input = Entry(self.root, width=30)
        self.ner_input.pack(pady=(5,10), ipady=4)

        label2 = Label(self.root,text="Enter the term which like to search")
        label2.pack(pady=(10,10))
        
        self.ner_input2 = Entry(self.root, width=30)
        self.ner_input2.pack(pady=(5,10), ipady=4)
        
        ner_btn = Button(self.root, text='Search', command=self.do_ner_analysis)
        ner_btn.pack(pady=(10,10))
        
        self.ner_result = Label(self.root,text="",bg='#616a6b' ,fg='white')
        self.ner_result.pack(pady=(10,10))
        self.ner_result.configure(font=('verdana',16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10,10))
    

    def do_ner_analysis(self):
        text = self.ner_input.get()
        text2 = self.ner_input2.get()

        client = nlpcloud.Client("finetuned-llama-3-70b", "2b21ce3bf88d4ba196c69b7c42119a9cc8c33766", gpu=True)
        response = client.entities(text, searched_entity=text2)
        self.ner_result['text'] = response


    def emotion_gui(self):
        self.clear()

        heading = Label(self.root,text='NLPApp', bg='#616a6b', fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root,text='Summerization', bg='#616a6b', fg='white')
        heading2.pack(pady=(10,20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root,text="Enter the text")
        label1.pack(pady=(10,10))
        
        self.emotion_input = Entry(self.root, width=30)
        self.emotion_input.pack(pady=(5,10), ipady=4)

        
        emotion_btn = Button(self.root, text='Search', command=self.do_emotion)
        emotion_btn.pack(pady=(10,10))
        
        self.emotion_result = Label(self.root,text="",bg='#616a6b' ,fg='white')
        self.emotion_result.pack(pady=(10,10))
        self.emotion_result.configure(font=('verdana',16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10,10))
    

    def do_emotion(self):
        text = self.emotion_input.get()


        client = nlpcloud.Client("t5-base-en-generate-headline", "2b21ce3bf88d4ba196c69b7c42119a9cc8c33766", gpu=False)
        response = client.summarization(text)
        self.emotion_result['text'] = response
        
    



nlp = NLPApp()