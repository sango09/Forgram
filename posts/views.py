# Posts views

# Django
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yessica cortes',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',

    },
    {
        'title': 'Via Lactea',
        'user':{
            'name': 'C.vander',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        }, 
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo' : 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user':{
            'name': 'Thespianartist',
            'picture' : 'https://picsum.photos/60/60/?image=883'
        }, 
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo':'https://picsum.photos/500/700/?image=1076',
    }
]


def lists_posts(request):
    # lists existing posts.
    return render(request,'posts/feed.html',{'posts': posts},)