from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase the count
            worddictionary[word] += 1
        else:
            #Add word to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1))

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist),'sortedwords':worddictionary.items()})

def about(request):
    return render(request, 'about.html')
