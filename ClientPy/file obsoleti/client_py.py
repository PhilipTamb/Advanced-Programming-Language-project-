from urllib import request
from urllib import parse
from clientpyGraphic import *



def main():
    print("main:  ")
    response = request.urlopen("http://localhost:8000/hello")
    print('Response: ----> ', response)
    print('URL   :  ----> ', response.geturl())


    headers  = response.info()
    print("Date :  ----> ", headers["date"])
    print("Headers:   ----> ")
    print(headers)

    data = response.read().decode('utf-8')
    print("Lenght :  ----> ", len(data))
    print("Data :   ----> ")
    print(data)

    #query_args = { 'q' : 'query string', 'foo' : 'bar'}
    query_args = { 'q' : 'query string', 'foo' : 'bar'}
    encoded_args = parse.urlencode(query_args)
    print("Encoded:  ----> ", encoded_args)

    url = "http//:localhost:8000/" + encoded_args
    print( request.urlopen(url).read().decode('utf-8'))


if __name__ == "__main__":
    main()



