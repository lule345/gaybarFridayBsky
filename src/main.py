import os
import sys
from atproto import Client, models, Session, SessionEvent, Request
from dotenv import load_dotenv
from httpx import Timeout

def init():
    if not os.path.exists('./.env'):
        print('No API/env File found!')
        sys.exit()
    load_dotenv()
    key = os.getenv('APIKEY')
    user = os.getenv('USERNAME')
    request = Request(timeout=Timeout(timeout=10.0))
    client = Client(request=request)

    client.login(f'{user}', f'{key}')

    with open('gaybar.mp4', 'rb') as f:
        vid_data = f.read()
        aspect = {'height': 360, 'width': 480}
        client.send_video(text="It's Friday at the Gay Bar!", video=vid_data, video_alt="a video of the lain at the gay bar music video", video_aspect_ratio=aspect)
init()
