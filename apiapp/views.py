from django.shortcuts import render
from django.http import HttpResponse
import praw
reddit = praw.Reddit(client_id='TAS_yH676vQaog',
                     client_secret='D5JLtP-JTo21s4iNKgyE4L-P45I',
                     username='GameActivity',
                     password='',
                     user_agent='UniWebApp')
subreddit = reddit.subreddit('riskofrain')
hot_sub = subreddit.hot(limit=5)
post_array = []

for sub in hot_sub:
    sub_to_dict = {}
    sub_to_dict['title'] = sub.title
    sub_to_dict['ups'] = sub.ups
    print(sub_to_dict['title'])
    post_array.append(sub_to_dict)


def home(request):
    context = {
        'posts': post_array
    }
    return render(request, 'apiapp/home.html', context)


def about(request):
    return render(request, 'apiapp/about.html')
