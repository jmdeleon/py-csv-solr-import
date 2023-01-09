Example Apache Solr 8.x core to read a CSV file into a Solr index
using PySolr (Python Solr client)

This script and configuration is useful when you need additional
processing of the CSV values (like date-processing), beyond the
default Solr CSV file handler behaviour.

This is functionally similar to the DataImportHandler from earlier
versions of Solr, with CSV JDBC driver.
