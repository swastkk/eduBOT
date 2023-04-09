import pytube, whisper

from PIL import Image
from io import BytesIO
from quiz import app

from sumy.summarizers.luhn import LuhnSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

model = whisper.load_model("base")

def urlToText(url):
    data = pytube.YouTube(url)
    audioF = data.streams.get_audio_only()
    name = audioF.download()
            
    model = whisper.load_model("base")

    # timeStamps = model.
    audio_file = open(name, 'rb')
    audio_bytes = audio_file.read()
    text = model.transcribe(name)
    valuable = text['text']

    return audio_bytes, valuable 


# print("url se text trying ")
audioF , text = urlToText("https://youtu.be/J-nURWdlP_o")
print(text)
# print("url se text donme")

summary=" "

parser = PlaintextParser(text, Tokenizer('english'))
summarizer_1 = LuhnSummarizer()
summary_1 = summarizer_1(parser.document, 10)
for sentence in summary_1:
    summary += str(sentence)



print(summary)


question = input("question dedo : ")
context = summary 
qna_answer = gpt_3.qna(question , summary)


# print(qna_answer)
