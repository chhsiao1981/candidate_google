Goal
==========
這個 project 的目的是希望能夠利用 google search 來知道關於候選人們最重要的資訊.
(可能包括 facebook, wikipedia, 相關網站, 或是報導)

Data
=========
所有 extracted data 都放在 data/ 裡. 其中:

* mayor1: 直轄市長
* mayor2: 縣市長
* council1: 直轄市議員
* council2: 縣市議員
* town_leader: 鄉鎮市長
* town_representative: 鄉鎮市民代表
* aboriginal_leader: 直轄市山地原住民區長
* aboriginal_representative: 直轄市山地原住民區民代表
* village_leader: 村里長

Generate Data
==========
1. ./scripts/init.sh
2. ./scripts/gen_scripts.sh
3. (in bash) for j in ./scripts_op/*; do ./${j}; done

Reference Data
=========
這個 project 參考了以下 project 的 data:

https://github.com/kiang/elections
