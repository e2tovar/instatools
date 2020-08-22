from instaloader import Instaloader, Post, Hashtag
import get_post_hashtags as gh

# Function to check i=wether a post is shadowbaned
def is_shadowbaned(shortcode):
    L = Instaloader()
    POST = Post.from_shortcode(L.context, shortcode)
    DATE = POST.date
    #TODO regex from Link to get Shortcode
    DATE = POST.date
    hashtags_list = gh.get_hashtags(POST)
    shadow = False
    print(hashtags_list)
    for h in hashtags_list:
        count = 0
        #status
        print('analizando', h )
        H = Hashtag.from_name(L.context, h)
        if shadow == True:
            break
        #This K is to work with uncronological random posts
        k = 0
        #get the posts from the hashtag        
        posts = H.get_posts()     
        k_list = [] #----debug        
        for p in posts:
            count+=1
            postdate = p.date
            if p == POST:
                print(h, 'funded in', count)
                print('_____________________')
                break
            if postdate <= DATE:
                k += 1
                k_list.append(k) #--debug
                #accept until 300 uncronological random posts
                if k == 300:
                    shadow = True
                    print(h, 'baneado')
                    break
                else:
                    continue

if __name__ == '__main__':
    print('Paste the post link here:')
    short_code = input()
    is_shadowbaned(short_code)
    