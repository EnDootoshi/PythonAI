import random

class Responder:
    """
    応答クラスのスーパークラス
    """
    def __init__(self, name):
        """
        Responderオブジェクトの名前をnameに格納
        つまり、ユーザーの名前
        """
        self.name = name

    def response(self, input):
        """
        オーバーライドを前提としたメソッド
        空文字列を返す
        """
        return ''

    def get_name(self):
        return self.name



class RepeatResponder(Responder):
    """
    オウム返しのためのサブクラス
    """
    def response(self, input):
        """
        応答文字列を作って返す
        """
        return '{}ってなに？？'.format(input)


class RandomResponder(Responder):
    """
    ランダムな応答のためのサブクラス
    """
    def __init__(self, name):
        """
        Responderオブジェクトの名前を引数にして
        スーパークラスの__init__()を呼び出す
        ランダムに抽出するメッセージを格納したリストを作成
        """
        super().__init__(name)
        self.responses = ['これからなにするの？', '頑張ってね', 'すごいね']

    def response(self, input):
        """
        応答文字列を作って返す
        戻り値 ランダムに抽出した文字列
        """
        return (random.choice(self.responses))
