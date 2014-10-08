#!/bin/bash

mkdir -p scripts_op
python scripts/gen_scrapy.py 2014_candidates/直轄市長.csv > scripts_op/mayor1.sh
python scripts/gen_scrapy.py 2014_candidates/縣市長.csv > scripts_op/mayor2.sh
python scripts/gen_scrapy.py 2014_candidates/直轄市議員.csv > scripts_op/council1.sh
python scripts/gen_scrapy.py 2014_candidates/縣市議員.csv > scripts_op/council2.sh
python scripts/gen_scrapy.py 2014_candidates/鄉鎮市長.csv > scripts_op/town_leader.sh
python scripts/gen_scrapy.py 2014_candidates/鄉鎮市民代表.csv > scripts_op/town_representative.sh
python scripts/gen_scrapy.py 2014_candidates/直轄市山地原住民區長.csv > scripts_op/aboriginal_leader.sh
python scripts/gen_scrapy.py 2014_candidates/直轄市山地原住民區民代表.csv > scripts_op/aboriginal_representative.sh
python scripts/gen_scrapy.py 2014_candidates/村里長.csv > scripts_op/village_leader.sh

chmod 755 scripts_op/*.sh
