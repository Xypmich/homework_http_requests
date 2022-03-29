import requests

HEROES = ['Hulk', 'Captain America', 'Thanos']
stats = {}


def most_intelligence_hero(heroes_list, stats_dict):
    for hero in heroes_list:
        sh_stats = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{hero}')
        stats_dict[hero] = int(sh_stats.json()['results'][0]['powerstats']['intelligence'])
    stats_dict_sorted = sorted(stats_dict, key=stats_dict.get)
    winner = f'Самый умный герой - {stats_dict_sorted[-1]} с уровнем интеллекта {stats_dict[stats_dict_sorted[-1]]}'
    return winner


print(most_intelligence_hero(HEROES, stats))
