"""
Twitter/X Bot - Auto tweet, reply, dan analytics
"""

import os
import time
import logging
from datetime import datetime, timedelta
from typing import List, Optional
import tweepy

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TwitterBot:
    def __init__(self, api_key: str, api_secret: str, 
                 access_token: str, access_token_secret: str):
        """Initialize Twitter Bot dengan API credentials"""
        self.client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        # For v1.1 API (media upload, etc)
        self.auth = tweepy.OAuthHandler(api_key, api_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)
        
        logger.info("Twitter Bot initialized")
    
    def post_tweet(self, text: str, media_paths: Optional[List[str]] = None) -> str:
        """Post tweet dengan teks dan opsional media"""
        try:
            media_ids = None
            if media_paths:
                media_ids = []
                for path in media_paths:
                    media = self.api.media_upload(path)
                    media_ids.append(media.media_id)
            
            response = self.client.create_tweet(
                text=text,
                media_ids=media_ids
            )
            tweet_id = response.data['id']
            logger.info(f"Tweet posted: {tweet_id}")
            return tweet_id
            
        except Exception as e:
            logger.error(f"Error posting tweet: {e}")
            return ""
    
    def reply_to_mention(self, tweet_id: str, text: str) -> str:
        """Reply ke mention/tweet"""
        try:
            response = self.client.create_tweet(
                text=text,
                reply_to={'in_reply_to_tweet_id': tweet_id}
            )
            logger.info(f"Reply posted: {response.data['id']}")
            return response.data['id']
        except Exception as e:
            logger.error(f"Error posting reply: {e}")
            return ""
    
    def get_mentions(self, since_id: Optional[str] = None) -> List[dict]:
        """Get mention tweets since last check"""
        try:
            mentions = self.client.get_users_mentions(
                id=self.client.get_me().data.id,
                since_id=since_id,
                tweet_fields=['created_at', 'author_id']
            )
            return mentions.data or []
        except Exception as e:
            logger.error(f"Error getting mentions: {e}")
            return []
    
    def auto_follow(self, followers: List[int]) -> int:
        """Auto follow followers"""
        count = 0
        me = self.client.get_me().data.id
        
        for follower_id in followers[:10]:  # Rate limit
            try:
                self.client.follow(follower_id)
                count += 1
                time.sleep(1)  # Rate limiting
            except Exception as e:
                logger.warning(f"Could not follow {follower_id}: {e}")
        
        logger.info(f"Followed {count} users")
        return count
    
    def get_trending_hashtags(self, woeid: int = 1) -> List[str]:
        """Get trending hashtags"""
        try:
            trends = self.api.get_place_trends(woeid)
            hashtags = [t['name'] for t in trends[0]['trends'] 
                       if t['name'].startswith('#')]
            return hashtags[:10]
        except Exception as e:
            logger.error(f"Error getting trends: {e}")
            return []


def main():
    from dotenv import load_dotenv
    load_dotenv()
    
    bot = TwitterBot(
        api_key=os.getenv('TWITTER_API_KEY'),
        api_secret=os.getenv('TWITTER_API_SECRET'),
        access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
        access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    )
    
    # Example: Post a tweet
    bot.post_tweet("🤖 Bot is working! #automation #python")


if __name__ == "__main__":
    main()
