import praw
import time
import config

from .db import DB

class Search():
    def __init__(self):
        self.r = praw.Reddit(config.bot_name)
        self.subreddit = self.r.subreddit(config.subreddit)
        self.db = DB()

    def aio_stream(self, **kwargs):
        results = []
        results.extend(self.subreddit.new(**kwargs))
        results.extend(self.subreddit.comments(**kwargs))
        results.sort(key=lambda post: post.created_utc, reverse=True)

        return results

    def run(self):
        for item in praw.models.util.stream_generator(lambda **kwargs: self.aio_stream(**kwargs), skip_existing=True):
            if not self.db.find(item.author.id):
                self.subreddit.banned.add(item.author)
                self.db.add((item.author.id, item.author.name, time.time(), item.id,))