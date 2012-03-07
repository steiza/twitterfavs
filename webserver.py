import os
import urllib

import mako.lookup
import mako.template
import oauth2
import simplejson
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File
import txroutes


class Controller(object):

    def __init__(self, token_key, token_secret):
        self.__token_key = token_key
        self.__token_secret = token_secret

        self.__consumer_key = '' # XXX - fill in your info here!
        self.__consumer_secret = '' # XXX - fill in your info here!

        consumer = oauth2.Consumer(key=self.__consumer_key,
                secret=self.__consumer_secret)

        token = oauth2.Token(key=self.__token_key, secret=self.__token_secret)
        self.__client = oauth2.Client(consumer, token)

        self.__template_lookup = mako.lookup.TemplateLookup(directories=[
                os.path.join(os.path.dirname(__file__), 'templates')])

    def get_index(self, request):
        favorites_url = 'https://api.twitter.com/1/favorites.json'
        response, content = self.__client.request(favorites_url, method='GET')

        content = simplejson.loads(content)

        template = self.__template_lookup.get_template('index.mako')
        return template.render(content=content).encode('utf8')


def setup_webserver(port):
    controller = Controller(
            token_key='', # XXX - fill in your info here!
            token_secret='', # XXX - fill in your info here!
            )

    dispatcher = txroutes.Dispatcher()

    dispatcher.connect('get_index', '/', controller=controller,
            action='get_index', conditions=dict(method=['GET']))

    static_path = os.path.join(os.path.dirname(__file__), 'static')
    dispatcher.putChild('static', File(static_path))

    site = Site(dispatcher)
    reactor.listenTCP(port, site)


if __name__ == '__main__':
    setup_webserver(8000)
    reactor.run()
