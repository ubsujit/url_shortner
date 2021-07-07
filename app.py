########################################################
#                                                      #
# This is a flask application which accepts URL from   #
# user and returns the shortened URL. If the URL is    #
# already shortned then returns the existing short URl #
########################################################
from flask import Flask, request

app = Flask(__name__)

@app.route('/url_shortner/<string:url>', methods=['GET'])
def shorten_url(url):
    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
