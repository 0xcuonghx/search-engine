@echo off
echo Start crawling ...
python ./crawler/vnexpress/run.py
echo Start importing to solr-8.5.0 ...
for /f "tokens=1-4 delims=/ " %%i in ("%date%") do (
     set dow=%%i
     set month=%%j
     set day=%%k
     set year=%%l
)
set datestr=%year%-%month%-%day%
curl "http://localhost:8983/solr/IT4853/update?commit=true&trim=true" --data-binary @C:\IR-IT4853\crawler\data\%datestr%.csv -H "Content-type:application/csv"
echo Success!!
pause
