import tkinter as tk
from maki import *
import sys

"""
グローバル変数の定義
"""
entry = None
response_area = None
lb = None
action = None
maki = Maki('maki')
on_canvas = None
maki_images = []


def putlog(str):
    """
    対話のログをリストボックスに追加する関数
    strには入力文字または応答メッセージが入る
    """
    lb.insert(tk.END, str)


def prompt():
    """
    堀北真希のプロンプトを作る関数
    """
    m = maki.name
    if (action.get()) == 0:
        m += '：(' + maki.responder.name + ')'
    return m + '> '


def chagImg(img):
    """ 画像をセットする関数
    """
    canvas.itemconfig(
    on_canvas,
    image = maki_images[img],   # イメージオブジェクトを指定
    )
    canvas.update()


def change_looks():
    em =maki.emotion.mood
    if -5 <= em <= 5:
        chagImg(0)
    elif -10 <= em < -5:
        chagImg(1)
    elif -15 <= em < -10:
        chagImg(2)
    elif 5 <= em <= 15:
        chagImg(3)


def talk():
    """
    対話を行う関数
    ①Makiクラスのdialogue()を実行して応答メッセージを取得
    ②入力文字列および応答メッセージをログに出力
    """
    value = entry.get()
    if not value:
        response_area.configure(text='どうしたの？')
    elif value == 'さよなら' or value == 'バイバイ':
        response = 'うん、またね'
        response_area.configure(text=response)
        putlog('> '+ value)
        putlog(prompt() + response)
        entry.delete(0, tk.END)
        root = tk.Tk()
        root.geometry('70x56+600+200')
        button = tk.Button(root, text='Exit', command=sys.exit)
        button.pack(expand=1)
        root.mainloop()
    else:
        response = maki.dialogue(value)
        response_area.configure(text=response)
        putlog('> '+ value)
        putlog(prompt() + response)
        entry.delete(0, tk.END)

    change_looks()


######################################################
#画面を描画する関数
######################################################

def window():
    # グローバル関数を使用するための関数
    global entry, response_area, lb, action, canvas, on_canvas, maki_images

    # メインウィンドウを作成
    root = tk.Tk()
    root.title('Talk With Maki Horikita : ')
    root.geometry('700x560+200+100')
    font = ('Helevetica', 14)
    font_log = ('Helevetica', 11)

    # メニューバーを作成
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    # 「ファイル」メニュー
    filemenu = tk.Menu(menubar)
    menubar.add_cascade(label='オプション', menu=filemenu)
    filemenu.add_command(label='閉じる', command=root.destroy)
    # オプションメニュー
    action = tk.IntVar()
    optionmenu = tk.Menu(menubar)
    menubar.add_cascade(label='オプション', menu=optionmenu)
    optionmenu.add_radiobutton(
        label = 'Responderを表示',      #アクション名
        variable = action,             #選択時の値を格納するオブジェクト
        value = 0                      #actionの値を０にする
    )
    optionmenu.add_radiobutton(
        label = 'Responderを表示しない',      #アクション名
        variable = action,             #選択時の値を格納するオブジェクト
        value = 1                      #actionの値を０にする
    )

    #キャンバスの作成
    canvas = tk.Canvas(
        root,
        width = 300,
        height = 300,
        bg = 'white',
        relief = tk.RIDGE,
        bd=2
    )
    canvas.place(x=370, y=0)

    # 表示するイメージを用意
    maki_images.append(tk.PhotoImage(file = 'maki_nomal.gif'))
    maki_images.append(tk.PhotoImage(file = 'empty.gif'))
    maki_images.append(tk.PhotoImage(file = 'angry.gif'))
    maki_images.append(tk.PhotoImage(file = 'happy.gif'))

    on_canvas = canvas.create_image(                    # キャンバス上にイメージを配置
        0,                                  # x座標
        0,                                  # y座標
        image = maki_images[0],                        # 配置するイメージオブジェクトを指定
        anchor = tk.NW                      # 配置の起点となる位置を左上隅に指定
    )

    #応答エリアを作成
    response_area = tk.Label(
        root,
        width = 33,
        height = 10,
        bg = 'pink',
        font = font,
        relief = tk.RIDGE,
        bd=2
    )
    
    response_area.place(x=370, y=305)

    #フレームの作成
    frame = tk.Frame(
                root,               # 親要素はメインウィンドウ
                relief=tk.RIDGE,    # ボーダーの種類
                borderwidth = 4     # ボーダー幅を設定
            )

    # 入力ボックスの作成
    entry = tk.Entry(
                frame,              # 親要素はフレーム
                width=50,           # 幅を設定
                font=font           # フォントを設定
            )
    entry.pack(side = tk.LEFT)      # フレームに左詰めで配置する
    entry.focus_set()               # 入力ボックスにフォーカスを当てる

    # ボタンの作成
    button = tk.Button(
                frame,              # 親要素はフレーム
                width=15,           # 幅を設定
                text='話す',        # ボタンに表示するテキスト
                command=talk        # クリック時にtalk()関数を呼ぶ
             )
    button.pack(side = tk.LEFT)     # フレームに左詰めで配置する
    frame.place(x=30, y=520)        # フレームを画面上に配置


    # リストボックスを作成
    lb = tk.Listbox(
            root,                   # 親要素はメインウィンドウ
            width=42,               # 幅を設定
            height=30,              # 高さを設定
            font=font_log           # フォントを設定
         )

    # 縦のスクロールバーを生成
    sb1 = tk.Scrollbar(
            root,                   # 親要素はメインウィンドウ
            orient = tk.VERTICAL,   # 縦方向のスクロールバーにする
            command = lb.yview      # スクロール時にListboxのyview()メソッドを呼ぶ
      )

    # 横のスクロールバーを生成
    sb2 = tk.Scrollbar(
            root,                   # 親要素はメインウィンドウ
            orient = tk.HORIZONTAL, # 横方向のスクロールバーにする
            command = lb.xview      # スクロール時にListboxのxview()メソッドを呼ぶ
          )

    # リストボックスとスクロールバーを連動させる
    lb.configure(yscrollcommand = sb1.set)
    lb.configure(xscrollcommand = sb2.set)
    # grid()でリストボックス、スクロールバーを画面上に配置
    lb.grid(row = 0, column = 0)
    sb1.grid(row = 0, column = 1, sticky = tk.NS)
    sb2.grid(row = 1, column = 0, sticky = tk.EW)

    # メインループ
    root.mainloop()



#=================================================
# プログラムの起点
#=================================================
if __name__  == '__main__':
    window()
