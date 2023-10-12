from dotenv import load_dotenv

from utils import os_environ_get

# Load DotEnvironment to load datas from .env file
load_dotenv()

# Telegram Account Datas
API_ID = os_environ_get('API_ID')
API_HASH = os_environ_get('API_HASH')

# Telegram Channel ID where we should perform an action
CHANNELS_AND_MESSAGES = {
    -1001037734971: 'ТуТ М0гЛо БыТь ВаШе Со0бЩеН3Е б0тЫ! \n\nКому-то реально данный пост полезно? \n Если да - 👍\n '
                    'Если нет -👎 \n \n Олег и Ильхом, чёт вы после меня пишите))'}
CHANNELS_ID_LIST = list(CHANNELS_AND_MESSAGES.keys())
CHANNELS_MESSAGE_LIST = list(CHANNELS_AND_MESSAGES.values())
