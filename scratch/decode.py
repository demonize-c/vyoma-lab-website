import base64
from bs4 import BeautifulSoup
with open('images/logo-transparent.svg', 'r') as f:
    soup = BeautifulSoup(f.read(), 'xml')
    b64 = soup.find('image')['href'].split(',')[1]
    with open('scratch/logo.png', 'wb') as f_out:
        f_out.write(base64.b64decode(b64))
