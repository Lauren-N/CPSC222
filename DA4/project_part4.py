import json
import requests
import html

"""
Name: Lauren Nguyen
Course: CPSC 222
Assignment: Data Assignment 4
Date: 10/26/2022
Description: Program works with APIS to pretty print data.
            I chose an API that takes movies Owen Wilson has starred in and said 'wow'.
            My end point was the full quote in the movie and what movie it is
"""
url = 'https://owen-wilson-wow-api.herokuapp.com/wows/random'
def main():
    response = requests.get(url=url)
    json_obj = json.loads(response.text)
    for full_quote_obj in json_obj:
        print()
        print(full_quote_obj['movie'], ':')
        print(full_quote_obj['full_line'])
        print()


if __name__ == '__main__':
    main()