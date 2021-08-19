from mediaaccount import MediaAccountClient
import sys,getopt
        
def main(argv):
    verbose = False
    apiKey = None
    all = False

    try:
        opts, args = getopt.getopt(argv,"hk:",["apikey=","verbose", "all"])
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
        elif opt in ("--all"):
            all = True

    client = MediaAccountClient(apiKey)

    if (all):
        scroll = client.scroll('ImportDatum', von = '04.08.2021', bis = '05.08.2021', maxItems=1000)

        currentIndex = 0
        for article, count in scroll:
            currentIndex += 1
            print(f'{currentIndex}/{count}: {article.inhalt.headline}')

        sys.exit()

    print(f'Request with ApiKey:{apiKey}')
    articles, nextlink, count = client.articles('ImportDatum', von = '01.05.2021', bis = '05.08.2021')

    print(f'{count} Gesamt')
    print(f'{len(articles)} Artikel empfangen ')
    print(f'nextlink: {nextlink} ')

    if (verbose):
        for article in articles:
            print(article.inhalt.headline)

if __name__ == "__main__":
   main(sys.argv[1:])