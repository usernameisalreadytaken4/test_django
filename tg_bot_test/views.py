import json

import requests
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt


def handle_update(update):
    chat_id = update['message']['chat']['id']
    send_message("Update", {
        'chat_id': chat_id,
        'message': 'Update',
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


def send_message(method, data):
    return requests.post(settings.TELEGRAM_API_URL + '/' + method, data)
