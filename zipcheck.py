import random
import urllib.request
import webbrowser
import threading

# Define the number of links to process in each batch
BATCH_SIZE = 200

def check_urls_batch(urls):
    for url in urls:
        check_url(url)

def check_url(url, count=0):
    try:
        urllib.request.urlopen("https://" + url, timeout=5)
        print("Found a working link: " + url)
        with open("workinglinks.txt", "a") as file:
            file.write(url + "\n")
    except urllib.error.HTTPError as e:
        print(f"{url} failed with the following error on attempt {count + 1}:")
        print(e)
        if count >= 2:
            return
        check_url(url, count=count + 1)
    except:
        pass

def main():
    h = urllib.request.urlopen("https://raw.githubusercontent.com/trickest/zip/main/zip-domains.txt")
    urls = [line.strip().decode('utf-8') for line in h]

    # Split the list of URLs into batches of BATCH_SIZE
    url_batches = [urls[i:i + BATCH_SIZE] for i in range(0, len(urls), BATCH_SIZE)]

    threads = []
    for url_batch in url_batches:
        thread = threading.Thread(target=check_urls_batch, args=(url_batch,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
