import json
import urllib.parse
import requests
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


def handle_update(update):
    chat_id = update['message']['chat']['id']
    text = update['message']['text']
    print(update)
    if text == '/start':
        send_message({
            'chat_id': chat_id,
            'text': 'проверка микрофона',
            'reply_markup': json.dumps({
                'inline_keyboard': [
                    [
                        {
                            "text": "Button2",
                            "web_app": {"url": "https://romulas.pythonanywhere.com/"}
                        },
                    ]
                ]
            })
        })
        set_button({
            'chat_id': chat_id,
            'menu_button': json.dumps({
                'type': 'web_app',
                'text': 'Займы',
                'web_app': {"url": "https://romulas.pythonanywhere.com/"}
            })
        })


@csrf_exempt
def telegram_bot(request):
    if request.method == 'POST':
        update = json.loads(request.body.decode('utf-8'))
        print(update)
        handle_update(update)
        return HttpResponse('ok')
    return HttpResponseBadRequest('Bad Request')


@csrf_exempt
def setwebhook(request):
    response = requests.post(
        settings.TELEGRAM_API_URL + "/setWebhook?url=" + 'https://romulas.pythonanywhere.com' + reverse_lazy(
            'telegram_bot')
    ).json()
    return HttpResponse(f"{response}")


def send_message(data):
    method = 'sendMessage'
    return requests.post(settings.TELEGRAM_API_URL + '/' + method, data)


def set_button(data):
    method = 'setChatMenuButton'
    return requests.post(settings.TELEGRAM_API_URL + '/' + method, data)


@csrf_exempt
def api_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        auth = data['_auth']
        user_data = json.loads(urllib.parse.parse_qs(auth)['user'][0])
        user_data['timestamp'] = timezone.now()
        user_data['event'] = 'visit_from_tg'
        return JsonResponse(user_data)
    return HttpResponse(f'ok, {request.method}')
