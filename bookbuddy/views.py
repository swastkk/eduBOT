from django.shortcuts import render
from django.http import HttpResponse
from .bookBuddy import getText
from .forms import BookbuddyForm
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer


def bookbuddy(request):
    if request.method == "POST":
        input = BookbuddyForm(request.POST, request.FILES)
        if input.is_valid():
            text = request.POST['text']
            if (len(request.FILES) == 0 or len(request.POST) == 0):
                if len(request.FILES) != 0:
                    file = request.FILES['file']
                    val, text = getText(file, "")
                    parser = PlaintextParser(text, Tokenizer('english'))
                    summarizer_1 = LuhnSummarizer()
                    summary_1 = summarizer_1(parser.document, 10)
                    output = ""
                    for sentence in summary_1:
                        output += str(sentence)
                    return HttpResponse(output)
                else:
                    parser = PlaintextParser(text, Tokenizer('english'))
                    summarizer_1 = LuhnSummarizer()
                    summary_1 = summarizer_1(parser.document, 10)
                    output = ""
                    for sentence in summary_1:
                        output += str(sentence)
                    return HttpResponse(output)
            else:
                return HttpResponse("kindly add only one out of 2")

    else:
        input = BookbuddyForm()
        return render(request, 'bookbuddy.html', {'form': input})
