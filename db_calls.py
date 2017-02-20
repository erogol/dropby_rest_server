from config import *
from pymongo import MongoClient
import falcon

client  = MongoClient(DB_ADDRESS, 27017)
db = client.dropby
col_feed = db.feeds
col_user = db.users
col_sessions = db.sessions

def db_insert_feed(feed):
    """
    Insert given feed to feed collection
    """
    col_feed.insert({"content":         feed['content'],
                    "user_id":          feed['user_id'],
                    "loc":              {'type': "Point",
                                         'coordinates':[float(feed['lon']),
                                                        float(feed['lat'])]},
                    "target_user_id":   feed['target_user_id'],
                    "revealed":         feed['revealed'],
                    "seen" :            False})

def db_get_closest_feeds_of_target_user(req, N):
    """
    Get closest N feeds to given location of a given target user
    """
    query = {}
    query['target_user_id'] = req['target_user_id']
    query['revealed'] = req['revealed']
    query['loc'] = {"$near":
                    {"$geometry":
                        {'type':"Point",
                         'coordinates': [float(req['lon']), float(req['lat'])]}
                    }
                 }
    if 'seen' in req.keys():
        query['seen'] = req['seen']
    print query
    items = col_feed.find(query).limit(N)
    return items


def db_get_inrange_feeds(loc, min_distance, max_distance):
    """
    Get all feeds in the given range
    """
    items = col_feed.find({"loc":{"$near":{coordinates: loc,
                                           "$maxDistance":max_distance,
                                           "$minDistance":min_distance,
                                  }}})
    return items

# def db_auth_token(self):
def db_auth_token_dec(func):
    def new_func(self, req, resp):
        # token = kwargs['token']
        # item = col_sessions.find_one({"token":token})
        # if item is None:
        #     raise falcon.HTTPError(falcon.HTTP_401, title="No such session", description="Session token does not match")
        # kwargs['session'] = item
        func(self, req, resp)
    return  new_func
