# /bin/bash

# extract exchange rates
echo "extracting new exchange rate values ..."
python3 import-currency-from-csv.py spot-data-1-new.csv > insert-into-currency-new.sql

# extract market data
echo "extracting new market data values ..."
python3 import-data-from-csv.py spot-data-1-new.csv > insert-into-marketdata-new.sql

# importing exchange rate
echo "importing new exchange rates ..."
# mariadb oilmarket -p < insert-into-currency.sql
python3 insert-into-oilmarket-mariadb.py insert-into-currency-new.sql

# importing market data
echo "importing new market data ..."
# mariadb oilmarket -p < insert-into-marketdata.sql
python3 insert-into-oilmarket-mariadb.py insert-into-marketdata-new.sql
