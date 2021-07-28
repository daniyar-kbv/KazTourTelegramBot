from typing import Optional
import requests
import constants
import time
import os


class RecognitionService:
    def send_short_audio(self, file_path: str) -> Optional[str]:
        print(f'reading file: {file_path}')
        with open(file_path, 'rb') as f:
            data = f.read()

        params = {
            'profanityFilter': True
        }
        print(f'creating params: {params}')

        print('sending request')
        response = requests.post(
            constants.YANDEX_RECOGNITION_SHORT_AUDIO_URL,
            data=data,
            params=params,
            headers=self.__get_headers())
        print(f'got response: {response.json()}')
        results = response.json().get('result')
        print(f'returning result: {results}')
        return results

    def send_long_audio(self, file_name: str) -> Optional[str]:
        params = {
            'config': {
                'specification': {
                    'profanityFilter': 'true'
                }
            },
            'audio': {
                'uri': constants.YANDEX_STORAGE_BUCKET_URL.format(bucket_name=constants.YANDEX_BUCKET_NAME,
                                                                  file_path=file_name)
            }
        }

        response = requests.post(
            constants.YANDEX_RECOGNITION_LONG_AUDIO_URL,
            json=params,
            headers=self.__get_headers())

        if response.json().get('code') is not None:
            print('Send long audio error:')
            print(response.json().get('message'))
            return None

        operation_id = response.json().get('id')
        return self.__get_results(operation_id)

    def __get_results(self, operation_id: str) -> str:
        response = requests.get(
            constants.YANDEX_RECOGNITION_RESULTS_URL.format(operation_id=operation_id),
            headers=self.__get_headers()
        )

        response_json = response.json()
        if response_json:
            if response_json.get('done'):
                response = response_json.get('response')
                if response:
                    chunks = response.get('chunks')
                    if chunks:
                        texts: [str] = []
                        for chunk in chunks:
                            alternatives = chunk.get('alternatives')
                            if alternatives:
                                alternative = alternatives[0]
                                if alternative:
                                    sentence = alternative.get('text')
                                    if sentence:
                                        texts.append(sentence)
                        return '. '.join(texts)
                return ''
            else:
                time.sleep(2)
                return self.__get_results(operation_id)
        return ''

    def __get_headers(self) -> dict:
        headers = {
            'Authorization': f'Api-Key {os.environ.get("API_SECRET")}'
        }
        print(f'creating headers: {headers}')
        return headers