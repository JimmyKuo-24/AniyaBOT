import matplotlib, datetime
matplotlib.use('Agg')
from imgurpython import ImgurClient

client_id = '377a9d38e49c276'
client_secret = '4d8d00604bd49e2636545127b6aac1629379cde0'
album_id = 'RtStSrw'
access_token = 'f6d7d978bf430c334b185c6a366fb0d0520f5537'
refresh_token = '0691940cf7d9f492462585fd53262f8ce6623530'

def showImgur(fileName):
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    
    config = {
        'album': album_id,
        'name': fileName,
        'title': fileName,
        'description': str(datetime.date.today())
    }

    try:
        print('[log:INFO]Uploading file to imgur...')
        imgur1 = client.upload_from_path(fileName + '.png', config=config, anon=False)['link']
        print('[log:INFO]Done upload.')
    except:
        imgur1 = ''
        print('[log:ERROR]Failed upload.')

    return imgur1
