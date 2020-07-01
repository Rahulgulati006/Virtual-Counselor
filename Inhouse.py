import tkinter
from tkinter import *
import random


questions = [
    "Proteins after digestion are converted into",
    "The chlorophyll in photosynthesis is used for",
    "Carbohydrates in the plants are stored in the form of",
    "Main site of photosynthesis",
    "The small pores present of leaf’s surface are called",
    "Photosynthesis is a",
    "Opening and closing of pores is a function performed by",
    "Which element is used in the synthesis of proteins?",
    "Temporary finger like extensions on amoeba are called",
    "Bile juice is secreted by",
    "Which of the following metals is present in the anode mud during the electrolytic refining of copper",
    "An element reacts with oxygen to give a compound with a high melting point. The compound is soluble in water. The element is likely to be",
    "The second most abundant metal in the earth’s crust is",
    "An alloy of Zn and Cu is dissolved in dil. HC1. Hydrogen gas is evolved. In this evolution of gas",
    "A greenish coating develops on copper utensils due to formation of",
    "Rusting of iron takes place in",
    "The bronze medals are made up of",
    "Silver articles becomes black on prolonged exposure to air. This is due to the formation of",
    "During smelting, an additional substance is added which combines with impurities to form a fusible product known as",
    "A student placed an iron nail in copper sulphate solution. He observed the reddish brown coating on the iron nail which is",
    "What is the rate of flow of electric charges called?",
    "Which of the following is the SI Unit of Electric Current?",
    "Which instrument is used for measuring electric potential?",
    "When one unit electric charge moves from one point to another point in an electric circuit, then the amount of work done in joules is known as?",
    "The hindrance presented by material of conductor to the smooth passing of electric current is known as:",
    "Focal length of plane mirror is",
    "Image formed by plane mirror is",
    "A concave mirror gives real, inverted and same size image if the object is placed",
    "Power of the lens is -40, its focal length is",
    "A concave mirror gives virtual, refract and enlarged image of the object but image of smaller size than the size of the object is",
    "Every quadratic polynomial can have at most",
    "In the given figure, PT is a tangent to a circle whose centre is O. If PT = 12 cm and PO = 13 cm then find teh radius of the circle.",
    "In the given figure, PT is a tangent to the circle and O is its centre. Find OP.",
    "In the given figure, ABC is a right triangle right angled at B such that BC = 6 cm and AB = 8 cm. Find the radius of the circle.",
    "Find the coordinates of the point equidistant from the points A(1, 2), B (3, –4) and C(5, –6).",
    "Find the value of P for which the point (–1, 3), (2, p) and (5, –1) are collinear.",
    "Find the distance of the point (–6, 8) from the origin.",
    "In what ratio of line x – y – 2 = 0 divides the line segment joining (3, –1) and (8, 9)?",
    "Two of the vertices of a ΔABC are given by A(6, 4) and B(–2, 2) and its centroid is G(3, 4). Find the coordinates of the third vertex C of the ΔABC.",
    "If p(x) is a polynomial of at least degree one and p(k) = 0, then k is known as",
    "Graph of a quadratic polynomial is a",
    "Zeroes of a polynomial can be determined graphically. No. of zeroes of a polynomial is equal to no. of points where the graph of polynomial",
    "A polynomial of degree n has",
    "The probability of a leap year selected at random contain 53 Sunday is:",
    "A bag contains 3 red and 2 blue marbles. A marble is drawn at random. The probability of drawing a black ball is :",
    "What is the probability that a number selected from the numbers (1, 2, 3,..........,15) is a multiple of 4?",
    "What are the total outcomes when we throw three coins?",
    "Construction of a cumulative frequency table is useful determining the",
    "The abscissa of the point of interaction of the ‘less than type’ and of the ‘more than type’ cumulative frequency curve of grouped data gives",
    "What should come in the blank?      Mode= (…………) –2 (mean)",
]

answers_choice = [
    [" Carbohydrates","Small globules","Amino acids","starch",],
    ["Absorbing light"," Breaking down water molecule"," No function","Reduction of CO2",],
    ["Glycogen","Starch","Glucose","Maltose",],
    ["Leaf","Stem","Chloroplast","Guard cells",],
    ["Stomata","Chlorophyll","Guard cells","None of these",],
    ["Catabolic process","Parabolic process","Amphibolic process","Photochemical lprocess",],
    ["Stomata","Chlorophyll","Chloroplast","Guard cells",],
    ["Hydrogen","Oxygen","Nitrogen","Carbon dioxide",],
    ["Cell membrane","Cell wall","Pseudopodia","Cilia",],
    ["Stomach","Pancreas","Small intestine","Liver",],
    ["Sodium","Aluminium","Gold","Iron",],
    ["calcium","carbon","iron","silicon",],
    ["oxygen","silicon","aluminium","iron",],
    ["only zinc reacts with dil. HC1","only copper reacts with dil. HC1","both zinc and copper react with dil. HC1","only copper reacts with water",],
    ["CuCo3","Cu(OH)2","Cu(OH)2.CuCO3","CuO",],
    ["ordinary water","distilled water","both ordinary and distilled water","none of the above",],
    ["Cu and Zn","Zn and Ni","Cu and Sn","Cu, Zn, Tn",],
    ["Ag2O","Ag2S","AgCN","Ag2O and Ag2S",],
    ["slag","mud","gangue","flux",],
    ["soft and dull","hard and flading","smooth and shining","rough and granular",],
    ["Electric potential","electric conductance","Electric current","none of these",],
    ["ohm","ampere","volt","faraday",],
    ["Ammeter","galvanometer","voltmeter","potentiometer",],
    ["Electric current","electric resistance","electric conductance","potential difference",],
    ["Resistance","Conductance","Inductance","None of these",],
    ["At infinity","Zero","Negative","None of these",],
    ["Real and erect","Real and inverted","Virtual and erect","Virtual and inverted",],
    ["At F","At infinity","At C","Beyond C",],
    ["4m","-40m","-0.25m","-25m",],
    ["At infinity","Between F and C","Between P and F","At E",],
    ["three zeros","one zero","two zeros","none of these",],
    ["5 cm","4 cm","6 cm","4.5 cm",],
    ["16 cm","15 cm","18 cm","17 cm",],
    ["3 cm","2 cm","4 cm","5 cm",],
    ["(2, 3)","(–1, –2)","(0, 3)","(1, 3)",],
    ["4","3","2","1",],
    ["8","11","10","9",],
    ["1 : 2","2 : 1","2 : 3","1 : 3",],
    ["(2, 3)","(4, 6)","(4, 3)","(5, 6)",],
    ["value of p(x)","zero of p(x)","constant term of p(x)","none of these",],
    ["straight line","circle","parabola","eclipse",],
    ["intersects y-axis","intersects x-axis","intersects y-axis or intersects x-axis","none of these",],
    ["only 1 zero","exactly n zeroes","atmost n zeroes","more than n zeroes",],
    ["53/ 366","1/7","2/7","53/365",],
    ["3/5","2/5","0","1/5",],
    ["1/5","4/5","2/15","1/3",],
    ["4","5","8","7",],
    ["mean","mode","median","all of the above",],
    ["mode","median","mean","all of the above",],
    ["3(median)","4(median)","2(median)","5(median)",],
] 

answers = [3,1,2,3,1,4,4,3,3,4,4,3,4,1,1,3,3,2,1,4,3,2,3,4,1,1,3,3,3,3,3,2,4,2,2,4,3,3,4,2,3,2,3,1,3,1,3,3,2,1] 

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 10):
        x = random.randint(0,49)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if score >= 35:
        img = PhotoImage(file="science.png")
        labelimage.configure(image=img)
        labelimage.image = img
        
    elif (score >= 15 and score < 35):
        img = PhotoImage(file="commerce.png")
        labelimage.configure(image=img)
        labelimage.image = img
        
    else:
        img = PhotoImage(file="humanities.png")
        labelimage.configure(image=img)
        labelimage.image = img
        


def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 10:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        # these two lines were just developement code
        # we don't need them
        calc()
    




def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times", 12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times", 12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times", 12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times", 12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()



root = tkinter.Tk()
root.title("Virtual Counsellor")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)


img1 = PhotoImage(file="virtualcounselor.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(100,30))



img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(50,50))

lblRules = Label(
    root,
    text = "You will be given 10 multiple choice questions\nOnce you select an answer that will be a final choice\nhence think before you select",
    width = 200,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()

root.mainloop()