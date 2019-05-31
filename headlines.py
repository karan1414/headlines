import feedparser
# used to parse xml data
from flask import Flask


app = Flask(__name__)
#instance of Flask obj using module name as parameter


RSS_FEED = {
            'thewire':'https://thewire.in/rss',
            'quint':'https://www.thequint.com/feed'
            }



@app.route('/<publication>')
def quint(publication):
    return get_news(publication)


def get_news(publication):
    feed = feedparser.parse(RSS_FEED[publication])
    first_article = feed['entries'][0]
    return """
                <html>
                    <body>
                        <h1> Headlines </h1>
                        <b>{0}</b><br>
                        <i>{1}</i><br>
                        <p>{2}</p> <br/>
                    </body>
                </html>
                """.format(first_article.get("title"),first_article.get("published"),first_article.get("summary"))


if __name__ == '__main__':
    app.run(debug=True)
#run our code only / is True only when when our application is run directly.
#prevents python script from being run unintentionally when imported to other python files
