#Tkinterインポート～いつもの設定
import tkinter as tk

root = tk.Tk()
root.resizable(width=False,height=False)#ウィンドウサイズの変更を不可に
root.title("BMI APP")
root.geometry("250x150")

#BMIを計算する関数の作成
def calc(weight,height):
    return weight/(height**2)
def check(bmi):
    if bmi < 18.5: return "低体重BMIは",round(bmi,2),"です"
    elif bmi < 25.0: return "普通体重BMIは",round(bmi,2),"です"
    elif bmi < 30.0: return "肥満度1BMIは",round(bmi,2),"です"
    elif bmi < 35.0: return "肥満度2BMIは",round(bmi,2),"です"
    elif bmi < 40.0: return "肥満度3BMIは",round(bmi,2),"です"
    else :return "肥満度4BMIは",round(bmi,2),"です"

#ハンドラ関数（特定のイベントが起きた時に実行する関数）の作成
def judgement():
    w = float(weight.get())
    h = float(height.get())/100
    label_5["text"] = check(calc(w,h))
    
#ラベルウィジェットの作成（配置は最後に行う）
label_1 = tk.Label(root,text = "体重")
label_2 = tk.Label(root,text = "Kg")
label_3 = tk.Label(root,text = "身長")
label_4 = tk.Label(root,text = "cm")
label_5 = tk.Label(root,text = "体重と身長を入力して下さい。")
#エントリーウィジェット（入力する値）の作成（配置は最後に行う）
weight = tk.Entry(width = 5)
height = tk.Entry(width = 5)
#ボタンウィジェットの作成　ボタンクリックでハンドラ関数JudGementを呼び出す（配置は最後）
button = tk.Button(root,text="BMI判定",command=judgement)
#各列の割合を指定
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
#各行の割合を指定
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
#ラベルやボタン等のウィジェットの配置
label_1.grid(column=0,row=0,sticky=tk.E)
weight.grid(column=1,row=0)
label_2.grid(column=2,row=0,sticky=tk.W)
label_3.grid(column=0,row=1,sticky=tk.E)
height.grid(column=1,row=1)
label_4.grid(column=2,row=1,sticky=tk.W)
button.grid(column=0,row=2,columnspan=3)
label_5.grid(column=0,row=3,columnspan=3)

root.mainloop()