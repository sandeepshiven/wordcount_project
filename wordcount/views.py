from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter


def home(request):
    return render(request,"home.html")

def count(request):
    fulltext = request.GET['fulltext']
    if(fulltext==''):
        output = {"fulltext":fulltext,"count":0,"words":[('','')],"most":''}
        return render(request,"count.html",output)
    count = fulltext.split()
    word_count = Counter(count)
    most_used = word_count.most_common(1)
    word_count = sorted(word_count.items(),key=lambda x:x[1],reverse=True)
    
    output = {"fulltext":fulltext,"count":len(count),"words":word_count,"most":most_used[0][0]}
    return render(request,"count.html",output)



def about(request):
    return render(request, "about.html")


