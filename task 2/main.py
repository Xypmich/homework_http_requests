import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=headers,
                     params={'path': '!!!Homework_Komarov'})
        if os.path.isfile(file_path):
            up_link = requests.get(
                'https://cloud-api.yandex.net/v1/disk/resources/upload', headers=headers,
                params={'path': f'!!!Homework_Komarov/{os.path.basename(file_path)}',
                'overwrite': 'true'}
            )
            requests.put(up_link.json()['href'], data=open(file_path, 'rb'))
        else:
            for file in os.listdir(file_path):
                up_link = requests.get(
                    'https://cloud-api.yandex.net/v1/disk/resources/upload', headers=headers,
                    params={'path': f'!!!Homework_Komarov/{file}', 'overwrite': 'true'}
                )
                requests.put(up_link.json()['href'], data=open(os.path.join(file_path, file), 'rb'))


if __name__ == '__main__':
    path_to_file = input('Введите путь к загружаемому файлу:\n')
    token = input('Введите токен Яндекс Диска:\n')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)