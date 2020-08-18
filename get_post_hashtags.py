import re
from instaloader import Instaloader, Post

# function to extract all the hashtags in from first 5 comments 
def extract_hashtags(text):    
    # the regular expression 
    regex = "#(\w+)"
    # extracting the hashtags
    hashtags_list = re.findall(regex, text)     
    return hashtags_list

# function to get hashtags from a post
def get_hashtags(post):
    #from caption
    hashtags_list = post.caption_hashtags
    #from 10 first comments
    comments = post.get_comments()
    for i, c in enumerate(comments):
        hashtags_list = hashtags_list + extract_hashtags(c.text)
        if i >= 10:
            break
    return hashtags_list

if __name__ == '__main__':
    L = Instaloader()
    print('Write post link here:')
    SHORTCODE = input()
    POST = Post.from_shortcode(L.context, SHORTCODE)
    print(get_hashtags(POST))
    