import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# heads = ['attitudes_count', 'comments_count', 'reposts_count', 'mid', 'raw_text',
#           'source', 'user.description', 'user.follow_count', 'user.followers_count',
#           'user.gender', 'user.id', 'user.mbrank', 'user.mbtype', 'user.profile_url',
#           'user.profile_image_url', 'user.screen_name', 'user.statuses_count',
#           'user.urank', 'user.verified', 'user.verified_reason']
# heads = ['attitudes_count,comments_count,', 'eposts_count,mid,', 'aw_text,sou',
#        'ce,use', '.desc', 'iption,use', '.follow_count,use', '.followe',
#        's_count,use', '.gende', ',use', '.id,use', '.mb', 'ank,use',
#        '.mbtype,use', '.p', 'ofile_u', 'l,use', '.p.1', 'ofile_image_u',
#        'l,use.1', '.sc', 'een_name,use', '.statuses_count,use', '.u',
#        'ank,use.1', '.ve', 'ified,use', '.ve.1', 'ified_', 'eason']
#
# df = pd.read_csv('./dataset/kriswu.csv','r',encoding='utf-8')
#
# print(df.loc[3])

with open('./dataset/kriswu.csv','r',encoding='utf-8') as f:
    f.readline()
    count = 0
    for line in f:
        if count == 10:break
        count += 1
        print(line)