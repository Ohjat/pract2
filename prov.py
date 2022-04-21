import  vk_api
from vk_api.audio import VkAudio

def main():
    vk_session = vk_api.VkApi('id pojty', 'passwor vedi')




    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        # Если происходит исключение во время аутентификации, то выводим ошибку и выходи
        print(error_msg)
        return
   #запись музыки в файд

    # Модуль для получения аудиозаписей без использования официального API.
    vkaudio = VkAudio(vk_session)

    a = open('text_mys_2.0.txt', 'w')
    for track in vkaudio.get_iter():
        try:
            a.write(f"{track['id']}\n")
            print(f"Название записаного трека : {track.get('title')}")
        except:
            print(f"Название не записаного трека : {track.get('title')}")

    a.close()
    # print(f"ID песни : {track['id']}")

if __name__ == '__main__':
    main()
