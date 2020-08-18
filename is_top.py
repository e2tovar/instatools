import get_post_hashtags as gh
from instaloader import Instaloader, Post, Hashtag

def is_top(hashtags_list):
    for h in hashtags_list:
        count = 0
        #status
        print('analyzing', h )
        H = Hashtag.from_name(L.context, h)
        
        #get the top posts from the hashtag        
        top_posts = H.get_top_posts()            
        for tp in top_posts:
            count+=1
            if tp == POST:
                print(h, 'funded in', count)            
                break
        print('-----------------------------------')

if __name__ == '__main__':
    L = Instaloader()
    print('Paste the post link here:')
    SHORTCODE = input()
    POST = Post.from_shortcode(L.context, SHORTCODE)
    is_top(gh.get_hashtags(POST))