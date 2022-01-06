from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import numpy as np
driver = webdriver.Chrome('chromedriver')


animes = [
    'shaman-king-2021',
    'komi-san-wa-comyushou-desu',
    'ousama-ranking']

episodes = [36,11,10]


anime_long_list = np.full((len(animes), 4), None)
anime_long_list[:,0] = animes
anime_long_list = anime_long_list.tolist()

def update_time(q = 'y'):
        for index,_ in enumerate(animes):
            driver.get(f'https://animeschedule.net/anime/{animes[index]}')
            driver.implicitly_wait(3)
            
            try:
                time = driver.find_element(By.XPATH, '//*[@id="countdown-wrapper"]/div/time').text
            except Exception as e:
                print(e)
                continue
            
            for j in ('d','h','m'):
                if j not in time:
                    globals()[j] = 0
                else:
                    for i in time.split():
                        if i.find(j) != -1:
                            globals()[j] = int(i[:-1])

            time_delta = datetime.timedelta(days = d, hours = h, minutes = m)
            anime_long_list[index] = [animes[index], episodes[index], time, time_delta]
            try:
                anime_long_list.sort(key=lambda x: x[3])
            except Exception as e:
                print(e)
                continue
        if q == 'y':
            driver.quit()
        for anime_list in anime_long_list[:]:
            print('\t'+str(anime_list[:-1])+',')

updated_anime = [
	['komi-san-wa-comyushou-desu', 11, '2d 23h 41m'],
	['shaman-king-2021', 36, '3d 17h 36m'],
	['ousama-ranking', 10, '4d 36m'],
        ]


def play_anime():
    update_time(q = 'n')
    anime, episode, _, time_delta = anime_long_list[0]
    hours, remainder = divmod(time_delta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"{int(hours)} hours, {int(minutes)} minutes left")
    if time_delta <= datetime.timedelta(hours = 1):
        if input(f"Ready for {anime} episode {episode}?: ").lower() == 'y':
            driver.get(f'https://www1.gogoanime.cm/{name}-episode-{episode}')
    else:
        print("It is not time to watch anime yet!")
        driver.quit()
        exit()

update_time()





















##driver.get('https://myanimelist.net/login.php')
##
##element = driver.find_element(By.ID, 'loginUserName')
##element.send_keys('guckyisme')
##
##element = driver.find_element(By.NAME, 'password')
##element.send_keys('haf071197')








