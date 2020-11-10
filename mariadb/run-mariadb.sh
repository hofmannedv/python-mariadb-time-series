# /bin/bash

# extract oiltype
echo "extracting oilypes ..."
python3 import-oiltype-from-csv.py spot-data-1.csv > insert-into-oiltype.sql

# extract exchange rates
echo "extracting exchange rate values ..."
python3 import-currency-from-csv.py spot-data-1.csv > insert-into-currency.sql

# extract market data
echo "extracting market data values ..."
python3 import-data-from-csv.py spot-data-1.csv > insert-into-marketdata.sql

# importing oiltype
echo "importing oilypes ..."
# mariadb oilmarket -p < insert-into-oiltype.sql
python3 insert-into-oilmarket-mariadb.py insert-into-oiltype.sql

# importing exchange rate
echo "importing exchange rates ..."
# mariadb oilmarket -p < insert-into-currency.sql
python3 insert-into-oilmarket-mariadb.py insert-into-currency.sql

# importing market data
echo "importing market data ..."
# mariadb oilmarket -p < insert-into-marketdata.sql
python3 insert-into-oilmarket-mariadb.py insert-into-marketdata.sql
