import functions
import time

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
DATA_STORE = 'data-tours.txt'

#if __name__ == "__main__":
while True:
    scraped = functions.scrape(URL)
    extracted = functions.extract(scraped, 'extract-tours.yaml', 'tours')
    print(extracted)

    content = functions.read(extracted, DATA_STORE)
    if extracted != "No upcoming tours":
        if extracted not in content:
            functions.store(extracted, DATA_STORE)
            functions.send_mail()
    time.sleep(5)

