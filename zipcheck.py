import random
import urllib.request
import webbrowser
import time
import threading

def check_url(url, count = 0):
    try:
        urllib.request.urlopen("https://" + url, timeout=30)
        print("Found a working link: " + url)
        with open("workinglinks.txt", "a") as file:
            file.write(url + "\n")
    except urllib.error.HTTPError as e:
        print(f"{url} failed with following error on attempt {count+1}:")
        print(e)
        if count >= 4:
          return
        check_url(url, count = count+1)
    except:
        pass

def main():
    h = urllib.request.urlopen("https://raw.githubusercontent.com/trickest/zip/main/zip-domains.txt")
    urls = [line.strip().decode('utf-8') for line in h]
    
    threads = []
    for url in urls:
        thread = threading.Thread(target=check_url, args=(url,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
