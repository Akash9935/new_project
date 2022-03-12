import instaloader
import bs4
ig = instaloader.Instaloader()
# for i in range(1,5):
    # with open('Book1.xlsx','w') as f:
        # for j in range(1):
            # f.write(f"download_profile{i}=True")


dp = input("Enter Insta username : ")


ig.download_profile(dp , profile_pic_only=True)