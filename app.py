########################################################
#                                                      #
# This is a flask application which accepts URL from   #
# user and returns the shortened URL. If the URL is    #
# already shortned then returns the existing short URl #
########################################################

import json
import uuid
import string
import random

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def welcome_msg():
    try:
        return "+++++++++Welcome to free URL shortening service+++++++++ \n \
        please enter below api call to shorten your URL \n \
        curl http://0.0.0.0:5000/url_shortner/url=google.com \n"
    except Exception as e:
        return "{}\n".format(e)

@app.route('/url_shortner/<string:url>', methods=['GET'])
def shorten_url(url):
    """This function checks if url is shortned else shortens the url

    Args:
        - url: url passed from input api

    Response:
        returns short_url

    Raises:
        it catches all kind of exceptions
    """
    try:
        # Check if URL is already shortened
        with open('url_data.json', "r") as fd:
            url_data = json.load(fd)
        for url_element in url_data:
            if url_element["url"] == url:
                return "URL alraedy exists, the shortned URL is {}\n".format(url_element["short"])
        # Shorten URL
        flag =1 
        while flag:
            status, response = generate_short_url()
            # Check if short url already assigned to other URLs
            if status:
                for url_element in url_data:
                    if url_element["short"] == response:
                        flag = 0
                        break
                url_dict = dict()
                url_dict["url"] = url
                url_dict["short"] = request.host_url + response
                url_data.append(url_dict)
                with open('url_data.json', "w") as fd:
                    fd.write(json.dumps(url_data))
                flag = 1
                return "{}\n".format(url_dict["short"])
            else:
                raise Exception("Internal server error- Failed to generate short URL")
    except Exception as e:
        return "Exception {}\n".format(e)

def generate_short_url():
    try:
        char_pool = string.ascii_letters + string.digits
        hash_string = ''.join(random.choice(char_pool) for _ in range(6))
        return True, hash_string
    except Exception as e:
        return False, "failed to generate hascode"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
