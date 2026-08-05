# gaybarFridayBsky
automatic bot on bluesky that posts lain at the gaybar every friday (UTC-4)

https://github.com/user-attachments/assets/71784fb9-ceaf-4bf5-94c3-d2c35bdd6abf


to note: this setup is meant for self-hosting/hosting on services. i am too lazy to bother with docker files, so you get to `git pull` instead!!

installation:
1. ensure pip is installed; see [install instructions here](https://pip.pypa.io/en/stable/installation/)
2. `pip install atproto`
3. `pip install dotenv`
4. setup the working directory; self-explanatory
5. ``git pull https://github.com/lule345/gaybarFridayBsky.git``
6. ``cd gaybarFridayBsky/src``
7. create a .env file with the format of: 

```
APIKEY=[APIKEY] # [APIKEY] should be your bluesky app password  
USER=[USER] # [USER] should be the email linked to your account
```

8. test/run the script via ``python main.py``

from here on, you can decide how to schedule the script yourself. i put this out here in order to open source the project, as well as a means to practice self-hosting.

Attributions:
- https://www.youtube.com/watch?v=yq0_ApTwNH4, "Lain at the Gay Bar" by purplepolecat
- https://pypi.org/project/atproto/, ATProto Python Library
- [Hack Club!](https://hackclub.com/)
