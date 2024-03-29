import requests
import os
import random
import string
import json
import threading
from requests.exceptions import SSLError
from datetime import datetime

def generate_random_name():
    event = random.randint(0, 4)
    if event == 0:
        return str(random.choice(names)).lower()
    elif event in [1, 2]:
        separator = ['-', '.', '_']
        return str(random.choice(names)).lower() + separator[random.randint(0, len(separator) - 1)] + str(
            random.choice(names)).lower()
    else:
        return str(random.choice(names)).lower() + random.choice(string.digits) + random.choice(string.digits)

def generate_random_password():
    event = random.randint(0, 6)
    if event == 0:
        return ''.join(random.choice(chars) for i in range(random.randint(7, 15)))
    elif event in [1, 2]:
        return random.choice(dictionary) + random.choice(dictionary) + random.choice(string.digits)
    elif event in [3, 4]:
        return random.choice(dictionary) + random.choice(string.digits)
    else:
        return random.choice(string.digits) + random.choice(dictionary) + random.choice(names)
    
def generate_random_credit_card():
    return ''.join(random.choice(string.digits) for i in range(16))

def generate_random_credit_card_expiration():
    return ''.join(random.choice(string.digits) for i in range(4))

def generate_random_credit_card_cvv():
    return ''.join(random.choice(string.digits) for i in range(3))

def run():
    proxy = None
    while True:
        if use_proxy == 'y':
            proxy = f'socks5://{random.choice(proxy_list)}'
        if formDataNameLoginName == 'u':
            username = generate_random_name()
        if formDataNameLoginName == 'e':
            username = generate_random_name() + '@' + random.choice(emails) + \
                '.' + random.choice(ext)
        password = generate_random_password()
        try:
            r = requests.post(url, headers=headers, allow_redirects=False, data={
                str(formDataNameCookie): str(headers['Cookie']),
                str(formDataNameContentType): str(headers['Content-Type']),
                str(formDataNameLogin): username,
                str(formDataNamePass): password,
            }, proxies=dict(http=proxy, https=proxy))
            date = datetime.today().strftime('%H:%m:%S')
            if r.status_code == 403 or r.status_code == 429 or r.status_code == 500 or r.status_code == 502 or r.status_code == 503 or r.status_code == 504:
                print(f'[{date}] {r.status_code} {r.reason} {r.url}')
                proxy = f'socks5://{random.choice(proxy_list)}'
                if r.status_code == 429:
                    print(f'[{date}] {username}:{password} - {r.status_code}; You are being rate limited!')
                continue
            print(
                f'{date}> [Result: {r.status_code}] - [{formDataNameLogin}: {username}] - [{formDataNamePass}: {password}] [Proxy: {proxy}]')
        except SSLError as e:
            proxy = f'socks5://{random.choice(proxy_list)}'
            # print('Error: URL can no longer be reached..')
        except Exception as e:
            proxy = f'socks5://{random.choice(proxy_list)}'
            continue
            # print(f'Error: {e.__class__.__name__}')

mrfish_display = """.
 \033[93m       /`·.¸          \033[0m
 \033[93m      /¸...¸`:·       \033[0m \033[93mMrFish\033[0m - Discord Nitro Phishing Form Spammer w/header support
 \033[93m  ¸.·´  ¸   `·.¸.·´)  \033[0m
 \033[93m : © ):´;      ¸  {   \033[0m By Daan Van Essen#1337 / Amadeus
 \033[93m  `·.¸ `·  ¸.·´\`·¸)  \033[0m Modified by rens#6161
 \033[93m      `\\\\´´\¸.·´    \033[0m
."""
mrfish_display_list = mrfish_display.split('\n')

if __name__ == '__main__':
    for i in mrfish_display_list:
        os.system(f'echo{i}')
    url = input(' Form Request URL: ')
    headers = {'Cookie': '{formDataNameCookie}', 'Content-Type': '{formDataNameContentType}'}
    formDataNameLogin = input(' Form Data Username [Account/Email] Name: ')
    formDataNamePass = input(' Form Data Password Name: ')
    formDataNameCookie = input(' Required Cookie: ')
    formDataNameContentType = input(' Content Type: ')
    while True:
        formDataNameLoginName = input(' Is this a username or email? [u/e]: ')
        if formDataNameLoginName.lower() in ('u', 'e'):
            if formDataNameLoginName.lower() == 'u':
                break
            if formDataNameLoginName.lower() == 'e':
                break
        else:
            print(' That is not a valid option')
            continue
    while True:
        threads = input(' Threads [recommend max of 32]: ')
        if threads.isdigit() and 1 <= int(threads) <= 5000:
            threads = int(threads)
            break
        else:
            print(' Please enter a valid number between 0 and 5001')
            continue
    while True:
        use_proxy = input(' Enable Proxy [Y/N]: ')
        if use_proxy.lower() in ('y', 'n'):
            if use_proxy.lower() == 'y':
                print('Since you are using the proxy setting, you might experience slower performance and less stability; however, we do filter status requests.\n\n')
                print('A kind note to the proxy setting:\nThis setting might--on some sites--seem to not be working as you have not seen any recent requests.\n\n')
                break
            if use_proxy.lower() == 'n':
                break
        else:
            print(' That is not a valid option')
            continue
    while True:
        credit_card = input(' Generate credit card numbers? [Y/N]: ')
        if credit_card.lower() in ('y', 'n'):
            if credit_card.lower() == 'y':
                print('Generating credit card numbers..')
                break
            if credit_card.lower() == 'n':
                break
        else:
            print(' That is not a valid option')
            continue
    if credit_card.lower() == 'y':
        while True:
            credit_card_expiration = input(' Generate credit card expiration dates? [Y/N]: ')
            if credit_card_expiration.lower() in ('y', 'n'):
                if credit_card_expiration.lower() == 'y':
                    print('Generating credit card expiration dates..')
                    break
                if credit_card_expiration.lower() == 'n':
                    break
            else:
                print(' That is not a valid option')
                continue
    if credit_card.lower() == 'y':
        while True:
            credit_card_cvv = input(' Generate credit card CVV numbers? [Y/N]: ')
            if credit_card_cvv.lower() in ('y', 'n'):
                if credit_card_cvv.lower() == 'y':
                    print('Generating credit card CVV numbers..')
                    break
                if credit_card_cvv.lower() == 'n':
                    break
            else:
                print(' That is not a valid option')
                continue

    chars = string.ascii_letters + string.digits
    random.seed = (os.urandom(1024))

    names = json.loads(open('assets/names.json').read())
    emails = json.loads(open('assets/emails.json').read())
    ext = json.loads(open('assets/extensions.json').read())
    dictionary = json.loads(open('assets/dictionary.json').read())
    proxy_list = json.loads(open('assets/proxies.json').read())

for i in range(threads):
    t = threading.Thread(target=run)
    t.start()