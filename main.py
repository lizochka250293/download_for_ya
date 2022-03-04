import requests


class YandexUploader:
    token = None
    URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    header = None

    def __init__(self, token):
        self.token = token
        self.header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {token}'
        }
        print(self.header)

    def upload(self, file_path):
        """Метод загружает файл из file_path на яндекс диск"""
        self.file_path = file_path
        res = requests.get(url=f'{self.URL}?path={self.file_path}', headers=self.header)
        json_data = res.json()
        print(res.status_code, json_data)

        upload_response = requests.put(url=json_data['href'], data=open(file_path, 'rb'))

        return upload_response


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'readme.md'
    with open('t.txt', 'r', encoding="utf-8") as f:
        token = f.read()
        token = token.strip()
        print(token)
    uploader = YandexUploader(token=token)
    result = uploader.upload(file_path=path_to_file)
    print(result.status_code)
