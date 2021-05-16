import time
from datetime import datetime
import requests
from aiogram import Bot, types
import lxml.etree
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from bs4 import BeautifulSoup

import config

startTime = datetime.now()
bot = Bot(token=config.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)
ADMINS = config.ADMINS


# loger = str(datetime.today().time())[0:8]+' || '+message.from_user.full_name+' || @'+message.from_user.username+' || '+message.text

@dp.message_handler(commands=['state'])
async def state(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    url = 'https://sourceforge.net/projects/dft-builds/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    lst_updt = soup.find('div', class_='stats').find('time', class_='dateUpdated').text
    week_dwnl = soup.find('div', class_='stats').find('a', href='/projects/dft-builds/files/stats/timeline').text
    url = 'https://sourceforge.net/projects/dft-builds/files/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find('div', class_='btn-set').find('a',
                                                   class_='button green big-text download with-sub-label extra-wide').find(
        class_='sub-label').text[-0:-13]
    week_status = '<b>Последняя версия:</b> <u>' + name + '</u>\n' \
                                               '<b>Последнее обновление:</b> <u>' + lst_updt + '</u>\n' \
                                                                                     '<b>Количество скачиваний за прошедшую неделю:</b> <u>' + week_dwnl + '</u>\n'
    await message.answer(week_status, parse_mode='HTML')
    time.sleep(5)
    url = 'https://api.telegram.org/bot' + config.TOKEN + '/deleteMessage?chat_id=' + str(
        message.chat.id) + '&message_id=' + str(message.message_id)
    requests.get(url)


@dp.message_handler(commands=['status'])
async def status(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    status = "I am Alive!\n"
    status += "Uptime: " + str((datetime.now() - startTime))
    loger = str(datetime.today().time())[
            0:8] + ' || ' + message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text
    url = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=@dftcb_log&text=' + loger
    requests.get(url)
    await message.answer(status)
    time.sleep(5)
    url = 'https://api.telegram.org/bot' + config.TOKEN + '/deleteMessage?chat_id=' + str(
        message.chat.id) + '&message_id=' + str(message.message_id)
    requests.get(url)


@dp.message_handler(commands=['getbeta'])
async def get_beta(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    url = 'https://sourceforge.net/projects/dft-builds/files/beta/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    list = soup.find('tr', class_='file')
    name = list.find('span', class_='name').text[-0:-4]
    date = soup.find('abbr')
    urld = 'https://raw.githubusercontent.com/Dragonfly-Project/changelogs/master/' + name + '.txt'
    response = requests.get(urld)
    soup = BeautifulSoup(response.text, 'lxml')
    link = str(url + name + ".zip/download")
    beta = "💎 <b>Версия:</b> <u>" + name + "</u>\n"
    beta += "🛠 <b>Канал обновления:</b> <u>Beta</u>\n"
    beta += '🗒 <b>Список изменений:</b>\n' + soup.find('p').text + '\n'
    beta += "⬇ <b>Скачать:</b> " + link + "\n"
    loger = str(datetime.today().time())[
            0:8] + ' || ' + message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text
    url = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=@dftcb_log&text=' + loger
    requests.get(url)
    await message.answer(beta, parse_mode='HTML')
    time.sleep(5)
    url = 'https://api.telegram.org/bot' + config.TOKEN + '/deleteMessage?chat_id=' + str(
        message.chat.id) + '&message_id=' + str(message.message_id)
    requests.get(url)


@dp.message_handler(commands=['getstable'])
async def get_stable(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    url = 'https://sourceforge.net/projects/dft-builds/files/stable/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    list = soup.find('tr', class_='file')
    name = list.find('span', class_='name').text[-0:-4]
    urld = 'https://raw.githubusercontent.com/Dragonfly-Project/changelogs/master/' + name + '.txt'
    response = requests.get(urld)
    soup = BeautifulSoup(response.text, 'lxml')
    link = str(url + name + ".zip/download")
    stable = "💎 <b>Версия:</b> <u>" + name + "</u>\n"
    stable += "🛠 <b>Канал обновления:</b> <u>Stable</u>\n"
    stable += '🗒 <b>Список изменений:</b>\n' + soup.find('p').text + '\n'
    stable += "⬇ <b>Скачать:</b> " + link + "\n"
    loger = str(datetime.today().time())[
            0:8] + ' || ' + message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text
    url = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=@dftcb_log&text=' + loger
    requests.get(url)
    await message.answer(stable, parse_mode='HTML')
    time.sleep(5)
    url = 'https://api.telegram.org/bot' + config.TOKEN + '/deleteMessage?chat_id=' + str(
        message.chat.id) + '&message_id=' + str(message.message_id)
    requests.get(url)


@dp.message_handler(commands=['getlast'])
async def get_last(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    url = 'https://sourceforge.net/projects/dft-builds/files/'
    dwnl_link = 'https://sourceforge.net/projects/dft-builds/files/latest/download'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find('div', class_='btn-set').find('a', class_='button green big-text'
                                                               ' download with-sub-label extra-wide').find(
        class_='sub-label').text[-0:-13]
    url_builds = 'https://sourceforge.net/projects/dft-builds/'
    resp = requests.get(url_builds)
    sou = BeautifulSoup(resp.text, 'lxml')
    date = sou.find('div', class_='stats').find('time')
    urld = 'https://raw.githubusercontent.com/Dragonfly-Project/changelogs/master/' + name + '.txt'
    response = requests.get(urld)
    soup = BeautifulSoup(response.text, 'lxml')
    last = "💎 <b>Версия:</b> <u>" + name + "</u>\n"
    last += '🛠 <b>Канал обновления:</b> <u>Last</u>\n'
    last += "🗓 <b>Релиз:</b> <u>" + date.text + "</u>\n"
    last += '🗒 <b>Список изменений:</b>\n' + soup.find('p').text + '\n'
    last += '⬇ <b>Скачать:</b> ' + dwnl_link + '\n '
    loger = str(datetime.today().time())[
            0:8] + ' || ' + message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text
    url = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=@dftcb_log&text=' + loger
    requests.get(url)
    await message.answer(last, parse_mode='HTML')
    time.sleep(5)
    url = 'https://api.telegram.org/bot' + config.TOKEN + '/deleteMessage?chat_id=' + str(
        message.chat.id) + '&message_id=' + str(message.message_id)
    requests.get(url)

@dp.message_handler(commands=['post'])
async def post_channel(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    for ADMIN in ADMINS:
        if message.from_user.id == ADMIN:
            url = 'https://sourceforge.net/projects/dft-builds/files/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            ch = soup.find('div', class_='btn-set')
            channel = str(ch.find('a', class_='button green big-text download with-sub-label extra-wide'))
            if channel[126] == 'b':
                chan = 'Бета'
                vers = 'beta'
            else:
                chan = 'Стабильный'
                vers = 'stable'
            name = soup.find('div', class_='btn-set').find('a',
                                                           class_='button green big-text download with-sub-label extra-wide').find(
                class_='sub-label').text[-0:-13]
            dwnl_link = 'https://sourceforge.net/projects/dft-builds/files/'+vers+'/'+name+'.zip/download'
            urld = 'https://raw.githubusercontent.com/Dragonfly-Project/changelogs/master/' + name + '.txt'
            response = requests.get(urld)
            soup = BeautifulSoup(response.text, 'lxml')
            build = '❗ Новое обновление\n'
            build += '💎 Версия: ' + name + '\n'
            build += "🛠 Канал обновления: " + chan + "!\n"
            build += "🗓 Релиз: " + str(datetime.now().date()) + "\n"
            build += '🗒 Список изменений:\n' + soup.find('p').text + '\n'
            build += "⬇ Скачать: " + dwnl_link + "\n"
            url = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=@dft_official_dl&parse_mode=HTML&text=' + build
            requests.get(url)
            loger = str(datetime.today().time())[
                    0:8] + ' || ' + message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text
            url = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=@dftcb_log&text=' + loger
            requests.get(url)
            await message.answer("Done!")
            time.sleep(5)
            url = 'https://api.telegram.org/bot' + config.TOKEN + '/deleteMessage?chat_id=' + str(
                message.chat.id) + '&message_id=' + str(message.message_id)
            requests.get(url)


if __name__ == '__main__':
    executor.start_polling(dp)
