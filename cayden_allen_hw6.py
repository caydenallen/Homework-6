#!usr/bin/env python3
import sys
from urllib.request import urlopen

url = sys.argv[1]

def help():
    """
    Help Function
    """

    print("Usage is: ./cayden_allen_hw6 <file Input>")


def verify(url):
    """
    get_url info
    """

    if len(sys.argv) != 2:
        help()
    
        
        

def retrieve():
    """
    retrieving url
    """

    with urlopen(url) as log:
        print(url)
        print(log)


def main():
    # test function
      # help()
   # url = sys.argv[1:]
    
    verify(url)
    retrieve()  

if __name__=="__main__":
    main()
    exit(0)
