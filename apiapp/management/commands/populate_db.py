from django.core.management.base import BaseCommand
import httplib2
import json
from apiapp.models import SteamGameInfo

h = httplib2.Http(".cache")
gameList = json.loads(h.request('https://api.steampowered.com/ISteamApps/GetAppList/v2')[1].decode('utf-8'))['applist']['apps']


class Command(BaseCommand):
    def _create_info(self):
        for game in gameList:
            appid = game['appid']
            game_name = game['name']
            new_game = SteamGameInfo(title=game_name, appid=appid)
            new_game.save()
        print("Added games to DB")

    def handle(self, *args, **options):
        self._create_info()