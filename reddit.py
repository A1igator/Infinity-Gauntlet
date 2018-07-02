# Infinity Gauntlet

import praw
import time
import random

# reddit api login
reddit = praw.Reddit(client_id='API INFO',
                     client_secret='API INFO',
                     username='ThanosBanBot',
                     password='PASSWORD',
                     user_agent='ThanosBot 1.2')

Subreddit = reddit.subreddit("modabuse")
maximum = Subreddit.subscribers

def banHalf():
    counter = 0;
    while True:
        for comment in Subreddit.comments():
            if comment.author != None:
                if comment.author_flair_text != 'survived' and comment.author_flair_text != 'perished':
                    Random = random.randint(0,1)
                    if Random == 0:
                        Subreddit.flair.set(comment.author.name,'survived')
                    if Random == 1:
                        Subreddit.flair.set(comment.author.name,'perished')
                        Subreddit.banned.add(comment.author.name, ban_reason='The universe needs balance')
                    time.sleep(3)
                    counter+= 1
            for post in Subreddit.new():
                if post.author != None:
                    if post.author_flair_text != 'survived' and post.author_flair_text != 'perished':
                        Random = random.randint(0,1)
                        if Random == 0:
                            Subreddit.flair.set(post.author.name,'survived')
                        if Random == 1:
                            Subreddit.flair.set(post.author.name,'perished')
                            Subreddit.banned.add(post.author.name, ban_reason='The universe needs balance')
                        time.sleep(3)
                        counter+= 1
        if counter == maximum:
            return
banHalf()
