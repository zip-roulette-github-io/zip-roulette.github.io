import random
import urllib.request
import webbrowser

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
    for url in urls:
        check_url(url)

if __name__ == "__main__":
    main()
