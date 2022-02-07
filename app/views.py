from django.shortcuts import render
from django.http import HttpResponse
from .application import paraphrase

# Create your views here.
def index(req):
    return render(req, 'index.html')

def call_write_data(req):
    if req.method == 'GET':
        # write_data.pyのwrite_csv()メソッドを呼び出す。
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        paraphrase.write_csv(req.GET.get("input_data"))

        data = paraphrase.return_text()
        return HttpResponse(data)

def call_convert(req):
    if req.method == 'GET':
        # write_data.pyのwrite_csv()メソッドを呼び出す。
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        return HttpResponse(paraphrase.convert(req.GET.get("input_data")))

def call_paraphrase(req):
    if req.method == 'GET':
        # write_data.pyのwrite_csv()メソッドを呼び出す。
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        return HttpResponse(paraphrase.paraphrase(req.GET.get("input_data")))