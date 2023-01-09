Some CSV Tools

A few AWK and bash shell scripts to make the creation of Solr schema.xml fields and fields for the indexing Python script (index_data.py) from a CSV file a bit easier:

pyfields.awk - AWK script that generates field definitions for the indexing Python script (index_data.py)

schemafield.awk - AWK script that generates field tags for schema.xml . All fields are initially assumed to be non-multi-valued strings, and can be customized later to have different properties as necessary.

copyfield.awk - AWK script to generate copyField tags that copy all the fields to a field named "content". This allows for full-text search over a Drupal Search API index, as the "content" field is full-text searched by Drupal.

The scripts above generate tags based on the first line of a CSV file being fed to the script, where the first line contains column headers, which are then separated line by line, like this:

head -1 csvfile.csv | tr "," "\n" | awk -f pyfields.awk

The shell script "headings" calls the head and tr tools in a shell script to extract the list of fields from the first line of a CSV file.

The output of the above scripts can then be copied and pasted into the Python indexing script (index_data.py) or schema.xml where necessary.

Additionally, there is a "debom" shell script which removes the Byte-Order-Mark (BOM) sequence from the beginning of a file. The CSV JDBC driver seems to have trouble discarding the BOM when reading a CSV file, and so it needs to be removed when working with the driver.
