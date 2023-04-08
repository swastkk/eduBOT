from PyPDF2 import PdfReader
from gptKaam import GPT_3, load_dotenv
import os
from gtts import gTTS
from io import BytesIO
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

#  can modify to get detail by page
load_dotenv()
gpt_3 = GPT_3(os.getenv('OPENAI_API_KEY'))

total_content = ""


def getText(file_path, total_content):
    reader = PdfReader(file_path)
    # print(reader.numPages)
    val = len(reader.pages)
    for i in range(val):
        page = reader._get_page(i)
        page_content = page.extract_text()
        total_content += page_content

    return val, total_content


val, text = getText("know-india-booklet.pdf", "")
parser = PlaintextParser(text, Tokenizer('english'))
summarizer_1 = LuhnSummarizer()
summary_1 = summarizer_1(parser.document, 10)
print(summary_1)
for sentence in summary_1:
    print(sentence)


def sumToAudio(summary):
    audio = gTTS(summary)
    af = BytesIO()
    audio.write_to_fp(af)
    return af
