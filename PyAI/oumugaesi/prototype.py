class Maki:
    """
    堀北真希BOTの本体クラス
    """
    def __init__(self, name):
        """
        Makiオブジェクトの名前をnameに格納
        Responderオブジェクトを生成してresponderに格納
        """
        self.name = name
        self.responder = Responder('says')

    def dialogue(self, input):
        """
        応答オブジェクトのresponse()を呼び出して
        応答文字列を取得

        inputはユーザーに入力された文字列
        """
        return self.responder.response(input)

    def get_responder_name(self):
        """
        ユーザーに名前を返す
        """
        return self.responder.name

    def get_maki_name(self):
        """
        Makiの名前を返す
        """
        return self.name


class Responder:
    """
    応答クラス
    """
    def __init__(self, name):
        """
        Responderオブジェクトの名前をnameに格納
        つまり、ユーザーの名前
        """
        self.name = name

    def response(self, input):
        """
        応答文字列を作って返す
        """
        return '{}って何？？'.format(input)



#########################################################
##実行ブロック
#########################################################
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
