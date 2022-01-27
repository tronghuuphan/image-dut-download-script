import requests
import shutil
import os

year = '21'
faculty = ['101', '102', '103', '104', '105', '106', '107',
           '109', '110', '111', '117', '118', '121', '122', '123']

url_header = 'http://cb.dut.udn.vn/ImageSV/'

BASE_ROOT = os.getcwd()

for f in faculty:
    FOLDER_PATH = os.path.join(BASE_ROOT, f)
    if not os.path.exists(FOLDER_PATH):
        os.mkdir(FOLDER_PATH)

    os.chdir(FOLDER_PATH)

    for i in range(500):
        filename = f + year + "%04d" % i + '.jpg'
        url = url_header + year + '/' + filename

        r = requests.get(url, stream=True)
        if r.status_code == 404:
            print('{} not exists!'.format(filename))
            continue
        elif r.status_code == 200:
            r.raw.decode_content = True
            with open(filename, 'wb') as file:
                shutil.copyfileobj(r.raw, file)
            print('{} saved!'.format(filename))
