import os
import time

DIR = "./" # r'E:\OneDrive - Georgia Institute of Technology\gtRelated\github\twitterBot\cresci-rtbust-2019'
FILE = r'cresci-rtbust-2019.tsv'

with open(os.path.join(DIR, FILE)) as f:
    for line in f:
        user_id, label = line.strip().split()
        os.system("twarc timeline {} > {}.jsonl".format(user_id, user_id))
        time.sleep(3)
