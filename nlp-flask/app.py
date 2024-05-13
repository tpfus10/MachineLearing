from flask import Flask, render_template, request
import joblib, re
from konlpy.tag import Okt

app = Flask(__name__)
app.debug = True

okt = Okt()

model_lr = None 
tfidf_vector = None

model_nb = None 
dtm_vector = None

def load_lr():
    global model_lr, tfidf_vector
    model_lr = joblib.load("model/movie_lr.pkl")
    tfidf_vector = joblib.load("model/movie_lr_dtm.pkl")

def load_nb():
    global model_nb, dtm_vector
    model_nb = joblib.load("model/movie_nb.pkl")
    dtm_vector = joblib.load("model/movie_nb_dtm.pkl")

def tw_tokenizer(text):
    token_ko = okt.morphs(text)
    return token_ko

def lt_t(text):
    review = re.sub(r"\d+", " ", text)
    text_vector = tfidf_vector.transform([review])
    return text_vector

def lt_nb(text):
    stopwords=["은", "는", "이", "가"]
    review = text.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "")
    morphs = okt.morphs(review, stem=True) #토큰 분리
    test = " ".join(morph for morph in morphs if not morph in stopwords) #불용어 아닌 경우만 test에 저장
    test_dtm = dtm_vector.transform(test)
    return test_dtm

@app.route("/")
def index():
    menu = {
        "home":True,
        "senti":False
    }
    return render_template("home.html", menu=menu) #자동으로 templates 파일을 뒤짐->폴더 이름 바꾸면 안 됨

@app.route("/senti", methods=["GET", "POST"])
def senti():
    menu = {
        "home":False,
        "senti":True
    }
    if request.method == "GET":
        return render_template("senti.html", menu=menu) 
    else:
        review = request.form["review"]
        review_text = lt_t(review)
        lr_result = model_lr.predict(review_text)[0]
        review_text2 = lt_nb(review)
        nb_result = model_lr.predict(review_text2)[0]
        lr = "긍정"  if lr_result else  "부정"
        nb = "긍정"  if nb_result else  "부정"
        movie = {"review" : review, "lr" : lr, "nb": nb}
        return render_template("senti_result.html", menu = menu, movie=movie)

if __name__ == "__main__" :
    load_lr()
    load_nb()
    app.run()