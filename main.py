from instagrapi import Client

cl = Client()
cl.login_by_sessionid("1950230757:uGChasUCMwJR2k:14:AYelyUKztIN5k6LdJu85dhqVBxN59YpSUrsIESrmiw")

# media = client.photo_upload("./Black.png", caption="This is my story")

cl.photo_upload_to_story("black.jpg",)
