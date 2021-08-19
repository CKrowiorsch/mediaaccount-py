from client import MediaAccountClient
import sys,getopt
        
def main(argv):
    verbose = False
    apiKey = None   

    try:
        opts, args = getopt.getopt(argv,"hk:",["apikey=","verbose"])
    except getopt.GetoptError:
        print('error: app.py --apikey <apikey> --verbose')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print('app.py --apikey <apikey> --verbose')
            sys.exit()
        elif opt in ("-k", "--apikey"):
            apiKey = arg
        elif opt in ("--verbose"):
            verbose = True

    client = MediaAccountClient(apiKey)


    print(f'Request with ApiKey:{apiKey}')
    articles, nextlink, count = client.articles('ImportDatum', von = '01.01.2021', bis = '05.08.2021')

    print(f'{count} Gesamt')
    print(f'{len(articles)} Artikel empfangen ')

    if (verbose):
        for article in articles:
            print(article.inhalt.headline)

if __name__ == "__main__":
   main(sys.argv[1:])