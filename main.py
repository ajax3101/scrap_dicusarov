import requests
import fake_useragent
from bs4 import BeautifulSoup
import time
import os
import img2pdf



def get_images():

    s = requests.Session()
    url = 'https://dicusarov.net/%D0%9A%D0%BE%D0%BD%D1%86%D0%B5%D1%80%D1%82-%E2%84%961-cis-moll-%D0%B2-3-%D1%85-%D1%87%D0%B0%D1%81%D1%82%D1%8F%D1%85'
    user_agent = fake_useragent.UserAgent().random
    headers = {
        'user_agent': user_agent
    }

    res = s.post(url, headers=headers)
    #print (res)
    #time.sleep(20) # Пауза 20 сек :)

    # if not os.path.exists("data"):
    #     os.mkdir("data")

    # with open("data/page.html", "w", encoding="utf-8") as file:
    #     file.write(res.text)

    # with open("data/page.html", encoding="utf-8") as file:
    #      src = file.read()
    
    # soup = BeautifulSoup(src, 'lxml')

    if not os.path.exists("data"):
        os.mkdir("data")
    img_list = []
    for i in range(1, 77):
        url = f"http://dicusarov.net/info/im/225/{i}.jpg"
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f"media/{i}.jpg", "wb") as file:
            file.write(response)
            img_list.append(f"media/{i}.jpg")
            print(f"Downloaded {i} of 76")

    print("#" * 20)
    print(img_list)

    # create PDF file
    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))

    print("PDF file created successfully!")


def write_to_pdf():
    # print(os.listdir("media"))
    img_list = [f"media/{i}.jpg" for i in range(1, 77)]

    # create PDF file
    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))

    print("PDF file created successfully!")


def main():
    get_images()
    #write_to_pdf()


if __name__ == '__main__':
     main()

