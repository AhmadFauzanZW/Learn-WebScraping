import functions
import time

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#if __name__ == "__main__":
while True:
    scraped = functions.scrape(URL)
    extracted = functions.extract(scraped)
    print(extracted)

    content = functions.read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in content:
            functions.store(extracted)
            functions.send_mail()
    time.sleep(5)

