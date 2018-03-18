import urllib.request as req
import os




def download(url, filename):

    filename = filename + '.gz'

    opener = req.build_opener()
    opener.addheaders = [ ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]
    req.install_opener(opener)
    filename = os.path.join('C:/Users/Runes tryllemaskine/Desktop/4_Semester/Python/IMDB', filename)
    req.urlretrieve(url, filename)