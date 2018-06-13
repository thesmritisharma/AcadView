'''
#Question 1
ACCESS TOKENS-
The things that applications use to make API requests on behalf of a user.

The access token represents the authorization of a specific application to access specific parts of user's data.

They must be kept confidential in transit and in storage.
The only parties that should see the access tokens are the applications itself, the authorization server,
and resource server.

The application should ensure the storage of the access token is not accessible to other applications
on the same device.

---> Access token created on twitter.


#Question 2
www.google.com > 216.58.196.206
www.facebook.com > 157.240.16.35


#Question 4
An architect (read application developer) wanted to build a house(read application), so he prepared for all its
aspects including structure, plumbing, wiring, decors etc(read different libraries). He cant do all of the stuff
himself so he took help from various experts in those fields, who are really good at doing what they do. But he
needed communicate his needs and requirements face to face or via mail (read invoking API )so that they can cater
to his need and provide the asked service.  After some time a fellow Architect came and wanted to accomplish a
similar task but with a few add on features like swimming pool (a new library). He can conveniently use the
framework provided by our architect and add new features invoking any new service.

Carefully lets review-

A library is a collection of functions / objects that serves one particular purpose. you could use a library in a
variety of projects. (Various specialized services in our case)

An API is an interface for other programs to interact with your program or library  without having direct access.
( giving specifications for our need to various vendors in our case)

A framework is a collection of patterns and libraries to help with building an application.
(The master plan laid down by our architect for building a house )

A framework thus can be easily extended to plan a town having various houses, which may be same or similar
(having some new feature like swimming pool).

eg- Angular js- a JS framework may use many libraries like iniline editing of text using an exposed API
of that library.


#Question 5
import tweepy

consumer_key='**********************'
consumer_secret='********************************'

access_token='******************************'
access_token_secret='************************************'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = api.search('#ipl2018', lang="en", count=10, tweet_mode="extended")
print(tweets)
for tweet in tweets:
    print("--------------------")
    print(tweet.full_text)
    print("--------------------\n")

status = "Tweet tweet"
api.update_status(status=status)

#Question
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id='I********', client_secret='88888888888')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('2slphad0xy3sag1v3hzhb8iqb')

while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
