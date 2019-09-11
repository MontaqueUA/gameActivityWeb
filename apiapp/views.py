import json
from django.shortcuts import render
from django.http import HttpResponse
import httplib2
import praw
from django.utils.datetime_safe import date

reddit = praw.Reddit(client_id='TAS_yH676vQaog',
                     client_secret='D5JLtP-JTo21s4iNKgyE4L-P45I',
                     username='GameActivity',
                     password='',
                     user_agent='UniWebApp')
steam_key = '34DB82860786451A07EEA6D99E29E7E0'
gamespot_key = '5a2b3e37c87628f81dd57c3f8a440efc11dbf469'
h = httplib2.Http(".cache")
"""
resp, contents = h.request("https://www.gamespot.com/api/games/?api_key=" + gamespot_key + "&format=json&filter=publish_date:2016-01-01%7C2019-12-12", "GET")
i = 0
for content in contents:
    print(content)
"""
steam_resp, steam_games_user = h.request("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=34DB82860786451A07EEA6D99E29E7E0&steamid=76561198059634945&include_appinfo=true&format=json")
steam_games_user = json.loads(steam_games_user.decode('utf-8'))
"""for game in steam_games_user['response']['games']:
    name = json.loads(h.request("http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=" +
                                str(game['appid']) + "&format=json")[1].decode('utf-8'))
    print(name)
"""
context = {'games': steam_games_user['response']['games']}
# for steam_game in steam_games_user:
#     print(steam_game)

def home(request):
    return render(request, 'apiapp/home.html', context)


def about(request):
    return render(request, 'apiapp/about.html')


def account(request, search):
    return HttpResponse('<h1>the search was {}'.format(search))
    # return render(request, 'apiapp/account.html', search=search)
