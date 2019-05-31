import feedparser
# used to parse xml data
from flask import Flask,render_template
#to render templates render_template
app = Flask(__name__)
#instance of Flask obj using module name as parameter


RSS_FEED = {
            'thewire':'https://thewire.in/rss',
            'quint':'https://www.thequint.com/feed'
            }


@app.route('/')
@app.route('/<publication>')
def get_news(publication="thewire"):
    feed = feedparser.parse(RSS_FEED[publication])
    # first_article = feed['entries'][0]
    return render_template("home.html",
                            articles = feed['entries']
                            )


if __name__ == '__main__':
    app.run(debug=True)
#run our code only / is True only when when our application is run directly.
#prevents python script from being run unintentionally when imported to other python files
