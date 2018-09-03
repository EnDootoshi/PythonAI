from responder import *
from dictionary import *

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
        self.dictionary = Dictionary()
        self.emotion = Emotion(self.dictionary)

        # RandomResponderを生成
        self.res_random = RandomResponder('Random', self.dictionary)
        # RepeatResponderを生成
        self.res_repeat = RepeatResponder('Repeat', self.dictionary)
        # responderの初期値をRepeatResponderにする
        self.res_pattern =PatternResponder('Pattern', self.dictionary)


    def dialogue(self, input):
        """
        応答オブジェクトのresponse()を呼び出して
        応答文字列を取得

        inputはユーザーに入力された文字列
        """
        self.emotion.update(input)

        # 1~100をランダムに生成
        x = random.randint(1,100)
        if x <= 70:
            self.responder = self.res_pattern
        elif 71 <= x <=95:
            self.responder = self.res_random
        else:
            self.responder = self.res_repeat
        ## print(self.emotion.mood)  #機嫌値確認時に使用
        return self.responder.response(input, self.emotion.mood)


    def get_responder_name(self):
        """
        ユーザーにレスポンダーの名前を返す
        """
        return self.responder.name


    def get_maki_name(self):
        """
        Makiの名前を返す
        """
        return self.name



class Emotion:
    """
    Makiの感情モデル
    """
    MOOD_MIN = -15
    MOOD_MAX = 15
    MOOD_RECOVERY = 0.5
    
    def __init__(self, dictionary):
        """
        Dictionaryオブジェクトをdictionaryに格納
        機嫌値moodを０で初期化
        """
        self.dictionary = dictionary
        self.mood = 0


    def update(self, input):
        """
        ユーザーからの入力をパラメーターinputで受け取り
        パターン辞書にマッチさせて機嫌値を変動させる
        """
        for ptn_item in self.dictionary.pattern:
            if ptn_item.match(input):
                self.adjust_mood(ptn_item.modify)
                break

        if self.mood < 0:
            self.mood += Emotion.MOOD_RECOVERY
        else:
            self.mood -= Emotion.MOOD_RECOVERY


    def adjust_mood(self, val):
        """
        機嫌を増減させる
        """
        self.mood += int(val)
        if self.mood > Emotion.MOOD_MAX:
            self.mood = Emotion.MOOD_MAX
        elif self.mood < Emotion.MOOD_MIN:
            self.mood = Emotion.MOOD_MIN
