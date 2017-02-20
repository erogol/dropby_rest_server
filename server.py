"""
DropBy REST API implementation based on Falcon and Gunicorn WSGI
"""
import falcon
import json
import logging
logging.basicConfig(level=logging.INFO)

from db_calls import *
from bson.json_util import dumps # dumps ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class User:
    """
    Implements login, signup functions
    """
    def on_post(self, req, resp):
        pass

    def on_get(self, req, resp):
        pass


class Feed:
    """
    Implements feed post, get
    """

    @db_auth_token_dec
    def on_post(self, req, resp):
        logging.info("-> Feed insertion ...")

        ### Insert data to db
        try:
            db_insert_feed(req.params)
            resp.body = json.dumps({"status":200, "message":"Feed successfully inserted"})
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, title='Error', description="Feed cannot be inserted to DB")

    # @db_auth_token
    def on_get(self, req, resp):
        logging.info("<- Feed retrieval ...")

        ### get closest feed from db
        # try:
        ## Get closest feed to current location
        ### get revelaed or non-revealed feed
        feeds_iter = db_get_closest_feeds_of_target_user(req.params, int(req.params['N']))
        feeds = [feed for feed in feeds_iter]
        resp.body = dumps(feeds)
        # except Exception as ex:
        #     raise falcon.HTTPError(falcon.HTTP_400, title='Error', description="Feed cannot be retrieved")


api = falcon.API()
api.req_options.auto_parse_form_urlencoded = True
api.add_route('/user', User())
api.add_route('/feed', Feed())
