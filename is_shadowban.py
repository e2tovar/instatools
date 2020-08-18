from instaloader import Instaloader, Post, Hashtag
import get_post_hashtags as gh

# Function to check i=wether a post is shadowbaned
def is_shadowbane(hashtags_list):
    shadow = False
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
    L = Instaloader()
    print('Paste the post link here:')
    SHORTCODE = input()
    POST = Post.from_shortcode(L.context, SHORTCODE)
    DATE = POST.date
    is_shadowbane(gh.get_hashtags(POST))