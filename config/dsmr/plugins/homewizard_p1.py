import requests
from django.dispatch import receiver
from dsmr_backend.signals import backend_called
import dsmr_datalogger.services.datalogger

HOMEWIZARD_ENDPOINT = 'http://192.168.1.41:80/api/v1/telegram'
HOMEWIZARD_TIMEOUT = 5

@receiver(backend_called)
def handle_backend_called(**kwargs):
    response = requests.get(HOMEWIZARD_ENDPOINT, timeout=HOMEWIZARD_TIMEOUT)

    if response.status_code != 200:
        print(' [!] HomeWizard plugin: v1 telegram endpoint failed (HTTP {}): {}'.format(response.status_code, response.text))
        return

    dsmr_datalogger.services.datalogger.telegram_to_reading(data=response.text)
