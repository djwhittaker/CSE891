#I know that this does not work but I am going to go ahead and upload it so that I know how to upload things.
#I am getting very confused because I am using the example in Tutorial 5 on inverting dictionaries (although
#if you look at my code below you can see I gave up on that for the make_dates_dict, sorry) and although I can
#get the example code to work, it doesn't work when I try to apply it to the homework. For exaple, I tried to do
#fish=[row'fish'] just like the gender=row['gender'] but it told me that I couldn't use a string there. I give up.
#I guess I just need more help understanding this dictionary thing. The basic concept makes perfect sense, but
#all of these variable names are confusing me and I can't tell which ones are variables and which ones are labels
#anymore.

import csv, urllib

def load_csv(url):
  d = {}
  fp = urllib.urlopen(url)
  for row in csv.DictReader(fp):
     key = row['date']
     value = row['fish']

     x = d.get(key, [])
     x.append(value)
     d[key] = x

  return d

fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')
#for i in fish_d:
#  print i
  

def make_dates_dict(fish_d):
  dates_d = {}
  fp = urllib.urlopen('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')
  for row in csv.DictReader(fp):
    key = row['fish']
    value = row['date']
    x = dates_d.get(key, [])
    x.append(value)
    dates_d[key] = x
  return dates_d

def get_fishes_by_date(date):
  fishlist = []
  for date in fish_d:
    fishlist.append(fish)
  return fishlist

def get_dates_by_fish(dates_d, fish):
  dateslist = []
  for fish in dates_d:
    dateslist.append(date)
  return dateslist

# this code is outside the functions and USES the functions to
# load data and ask questions of the data.

fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')
dates_d = make_dates_dict(fish_d)

print get_fishes_by_date('1/1')
print get_dates_by_fish('plaice')
