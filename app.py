from datetime import datetime
import requests
from aiogram import Bot, types
import lxml.etree
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from bs4 import BeautifulSoup

import config

startTime = datetime.now()
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
ADMINS = config.ADMINS


# loger = str(datetime.today().time())[0:8]+' || '+message.from_user.full_name+' || @'+message.from_user.username+' || '+message.text

@dp.message_handler(commands=['status'])
async def process_start_command(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    status = "I am Alive!\n"
    status += "Uptime: " + str((datetime.now() - startTime))
    loger = str(datetime.today().time())[
            0:8] + ' || ' + message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text
    url = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=@dftcb_log&text=' + loger
    requests.get(url)
    await message.reply(status)


@dp.message_handler(commands=['getbeta'])
async def get_beta(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    url = 'https://sourceforge.net/projects/dft-builds/files/beta/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    list = soup.find('tr', class_='file')
    name = list.find('span', class_='name').text[0:29]
    date = soup.find('abbr')
    urld = 'https://raw.githubusercontent.com/Dragonfly-Project/changelogs/master/' + name + '.txt'
    response = requests.get(urld)
    soup = BeautifulSoup(response.text, 'lxml')
    link = str(url + name + ".zip/download")
    beta = "💎 Версия: " + name + "\n"
    beta += "🛠 Канал обновления: Beta\n"
    beta += "🗓 Релиз: " + date.text + "\n"
    beta += '🗒 Список изменений:\n' + soup.find('p').text + '\n'
    beta += "⬇ Скачать: " + link + "\n"
    loger = str(datetime.today().time())[
            0:8] + ' || ' + message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text
    url = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=@dftcb_log&text=' + loger
    requests.get(url)
    await message.reply(beta)


@dp.message_handler(commands=['getstable'])
async def get_stable(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    url = 'https://sourceforge.net/projects/dft-builds/files/stable/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    list = soup.find('tr', class_='file')
    name = list.find('span', class_='name').text[0:29]
    date = soup.find('abbr')
    urld = 'https://raw.githubusercontent.com/Dragonfly-Project/changelogs/master/' + name + '.txt'
    response = requests.get(urld)
    soup = BeautifulSoup(response.text, 'lxml')
    link = str(url + name + ".zip/download")
    stable = "💎 Версия: " + name + "\n"
    stable += "🛠 Канал обновления: Stable\n"
    stable += "🗓 Релиз : " + date.text + "\n"
    stable += '🗒 Список изменений:\n' + soup.find('p').text + '\n'
    stable += "⬇ Скачать: " + link + "\n"
    loger = str(datetime.today().time())[
            0:8] + ' || ' + message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text
    url = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=@dftcb_log&text=' + loger
    requests.get(url)
    await message.reply(stable)


@dp.message_handler(commands=['getlast'])
async def get_last(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    url = 'https://sourceforge.net/projects/dft-builds/files/'
    dwnl_link = 'https://sourceforge.net/projects/dft-builds/files/latest/download'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find('div', class_='btn-set').find('a', class_='button green big-text'
                                                               ' download with-sub-label extra-wide').find(
        class_='sub-label').text[0:29]
    url_builds = 'https://sourceforge.net/projects/dft-builds/'
    resp = requests.get(url_builds)
    sou = BeautifulSoup(resp.text, 'lxml')
    date = sou.find('div', class_='stats').find('time').text
    urld = 'https://raw.githubusercontent.com/Dragonfly-Project/changelogs/master/' + name + '.txt'
    response = requests.get(urld)
    soup = BeautifulSoup(response.text, 'lxml')
    last = "💎 Версия: " + name + "\n"
    last += '🛠 Канал обновления: Last\n'
    last += '🗓 Релиз :' + date + '\n '
    last += '🗒 Список изменений:\n' + soup.find('p').text + '\n'
    last += '⬇ Скачать: ' + dwnl_link + '\n '
    loger = str(datetime.today().time())[
            0:8] + ' || ' + message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text
    url = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=@dftcb_log&text=' + loger
    requests.get(url)
    await message.reply(last)


@dp.message_handler(commands=['post'])
async def post_channel(message: types.Message):
    print(message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text)
    for ADMIN in ADMINS:
        if message.from_user.id == ADMIN:
            url = 'https://sourceforge.net/projects/dft-builds/files/'
            dwnl_link = 'https://sourceforge.net/projects/dft-builds/files/latest/download'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            ch = soup.find('div', class_='btn-set')
            channel = str(ch.find('a', class_='button green big-text download with-sub-label extra-wide'))
            if channel[126] == 'b':
                chan = 'Бета'
            else:
                chan = 'Стабильный'
            name = soup.find('div', class_='btn-set').find('a',
                                                           class_='button green big-text download with-sub-label extra-wide').find(
                class_='sub-label').text[0:29]
            urld = 'https://raw.githubusercontent.com/Dragonfly-Project/changelogs/master/' + name + '.txt'
            response = requests.get(urld)
            soup = BeautifulSoup(response.text, 'lxml')
            build = '❗ Новое обновление\n'
            build += '💎 Версия: ' + name + '\n'
            build += "🛠 Канал обновления: " + chan + "!\n"
            build += "🗓 Релиз: " + str(datetime.now().date()) + "\n"
            build += '🗒 Список изменений:\n' + soup.find('p').text + '\n'
            build += "⬇ Скачать: " + dwnl_link + "\n"
            url = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=@dft_official&text=' + build
            requests.get(url)
            loger = str(datetime.today().time())[
                    0:8] + ' || ' + message.from_user.full_name + ' || @' + message.from_user.username + ' || ' + message.text
            url = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=@dftcb_log&text=' + loger
            requests.get(url)
            await message.reply("Done!")


@dp.message_handler()
async def loger_chat(message: types.Message):
    loger = str(datetime.today().time())[
            0:8] + ' || ' + message.from_user.full_name + ' || ' + message.from_user.username + ' || ' + message.text
    url = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=@dftcb_log&text=' + loger
    requests.get(url)


if __name__ == '__main__':
    executor.start_polling(dp)
