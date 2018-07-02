# Infinity Gauntlet

import praw
import time

# reddit api login
reddit = praw.Reddit(client_id='Rh_qf9ARRcVwxw',
                     client_secret='DoFKTulIjR85XhlGuDhnrJdCTc4',
                     username='ThanosBanBot',
                     password='PASSWORD',
                     user_agent='ThanosBot by u/XXAligatorXx')

Subreddit = reddit.subreddit("thanosdidnothingwrong")
maximum = Subreddit.subscribers

def banHalf():
    counter = 0;
    while True:
        for comment in Subreddit.comments(limit=1):
            if comment.author_flair_text != 'survived' and comment.author_flair_text != 'perished':
                if counter % 2 == 0:
                    Subreddit.flair.set(comment.author.name,'survived')
                else:
                    Subreddit.flair.set(comment.author.name,'perished')
                    Subreddit.banned.add(comment.author.name, ban_reason='The universe needs balance')
                time.sleep(3)
                counter+= 1
                if counter == maximum:
                    return
banHalf()
