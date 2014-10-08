#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import re
import os

out_prefix_map = {
    '直轄市長': 'mayor1',
    '縣市長': 'mayor2',
    '直轄市議員': 'council1',
    '縣市議員': 'council2',
    '鄉鎮市長': 'town_leader',
    '鄉鎮市民代表': 'town_representative',
    '直轄市山地原住民區長': 'aboriginal_leader',
    '直轄市山地原住民區民代表': 'aboriginal_representative',
    '村里長': 'villige_leader',
}


filename = sys.argv[1]
filename_prefix = re.sub('\.csv$', '', os.path.basename(filename))
out_prefix = out_prefix_map.get(filename_prefix, '')


def _gen_cmd(x):
    args = [x.get('name', ''), x.get('county', ''), 'facebook']
    out_filename = 'data/' + out_prefix + '/' + '.'.join(args) + '.csv'
    cmd = 'rm ' + out_filename + '; cd google_search; scrapy crawl google_search -a q=' + ','.join(args) + ' -o ../' + out_filename + '; cd ..'

    return cmd


df = pd.read_csv(filename, names=['county', 'name', 'party', 'number'])

df['county'] = df['county'].apply(lambda x: x.decode('utf-8')[0:3])
df['county'] = df['county'].apply(lambda x: x.encode('utf-8'))

df['cmd'] = df.apply(lambda x: _gen_cmd(x), axis=1)

df_out = df[['cmd']]

print "mkdir -p data/" + out_prefix

for (idx, row) in df_out.iterrows():
    print "%s" % (row.get('cmd', ''))
