from responder import *

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
        self.responder = RandomResponder('says') #RepeatResponder()ならオウム返しされる


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
