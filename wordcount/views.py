from django.http import HttpResponse
from django.shortcuts import render
import operator


def play(request):
    return render(request, 'play.html')

def count(request):
    fulltext =request.GET['fulltext']

    word_list = fulltext.split()

    worddict = {}
    for word in word_list:
        if word.lower() in worddict:
            #Increase
            worddict[word.lower()] += 1
        else:
            #Add to dict
            worddict[word.lower()] = 1

    sorted_words = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)


    return render(request, 'count.html', {'fulltext': fulltext, 
    'count': len(word_list), 'sorted_words': sorted_words})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')