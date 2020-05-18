#!/usr/bin/env python
# -*- coding: utf-8 -*-
#apaaanih coba deploy dah
import tweepy, time, sys

argfile = str(sys.argv[1])

#Masukan informasi berisi token dan consumer_key anda disini :
CONSUMER_KEY = '9dUYs7TrEI6mazA6T3YLBmF9E'
CONSUMER_SECRET = 'FI5rxNOQ2eLHsQOF7bMoYq0MetGdgYN52tYZwLhH6vQGppmSmK'
ACCESS_KEY = '975205761495179267-r8IrLn0ruPYhxBEF7xC9SxbwdcEkiat'
ACCESS_SECRET = 'yjv3wBawT8dhSPrSnVKPFxGanDYe8U90PkGN974HxdqxZ'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(20) #Tweet setiap 1 hari
