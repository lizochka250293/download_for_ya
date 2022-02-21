import requests


class YandexUploader:
    token = None
    URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    header = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}

    def __init__(self, token, URL, header):
        self.token = token
        self.URL = URL
        self.header = header

    def upload(self, file_path):
        """Метод загружает файл из file_path на яндекс диск"""
        self.file_path = file_path

        res = requests.get(f'{self.URL}/path={self.file_path}, headers=self.header).json()

        with open(file_path, 'r') as f:
            try:
                requests.post(res['href'], files={'file_path': f})
            except KeyError:
                print(res)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = requests.get(f'{URL}/upload?path={file_path}&overwrite={replace}', headers=header).json()
    with open('t.txt', 'r', encoding="utf-8") as f_1:
        token = f.read()
    uploader = YandexUploader(token)
    result = uploader.upload(path_to_file)
