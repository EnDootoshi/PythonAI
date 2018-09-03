from maki import *

########################################################
##実行ブロック
########################################################
def prompt(obj):
    """
    堀北真希のプロンプトを作る関数
    戻り値 'Makiオブジェクト名：応答オブジェクト ＞'
    """
    return obj.get_maki_name() + ' ' + obj.get_responder_name() + '>'

print('Maki Horikita System prototype : Maki') #プログラムの情報を表示
maki = Maki('MAKI')

while True:                         #対話処理開始
    inputs = input(' > ')
    if not inputs:
        print('バイバイ！')
        break
    res = maki.dialogue(inputs)     #応答文字列を取得
    print(prompt(maki), res)
