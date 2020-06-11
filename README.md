# IR-IT4853
Information Retrieval for IT4853 (HUST)

This project crawler data from vnexpress and store in solr for information retrival
solr: 
- index data
- fulltext-search

# list envirment
conda env list
# activate envirment
conda activate python38
# start solr
C:\solr-8.5.0\bin\solr.cmd start
# crawler
run.bat
# start app.py
pyhon search_engine/flask/app.py