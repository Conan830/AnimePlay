import requests
import urllib.parse
from AniPlay.plugins.other import emoji


class AnimeDex:
    def __init__(self) -> None:
        pass

    def search(query):
        url = 'https://api.anime-dex.workers.dev/search/' + \
            str(urllib.parse.quote(query))
        data =requests.get(url).json()['results']
        return data
        
    def anime(id):
        data =requests.get('https://api.anime-dex.workers.dev/anime/'+id).json()['results']

        title = data['name']
        text = f'{emoji()} **{title}**\n'
        img = data['image']

        item = []
        
        for i,j in item:
            text += '\n' + i.title().strip() +' : '+ j.strip().replace('\n', ' ')

        text += f"\nGenres: {data['genre']}"
        ep = int(data['episodes'])
        eplist =[]
        for i in range(1,ep+1):
            eplist.append((i,f'{id}-episode-{i}'))
            

        return img, text, eplist

    def episode(id):
        data =requests.get('https://api.anime-dex.workers.dev/episode/'+id).json()['results']
        text =data['name']
        surl =[
            ('Stream 1',data['stream']['sources'][0]['file']),
            ('Stream 2',data['stream']['sources_bk'][0]['file'])
            ]
        murl =data['servers'].items()

        return text, surl, murl
