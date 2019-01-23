
Example of usage Django and Citus.
----------------------------------



1. Install Citus

    https://omidraha.com/en/latest/src/citus/tips.html#install-citus-on-multi-machine-cluster-on-ubuntu

2. Run this command on `master` and each one of `workers`:


```
    $ createdb citus_exp

    $ psql -d citus_exp -c "CREATE EXTENSION citus;"

```

3. Register `workers` for this `citus_exp` db

```
    $ psql -d citus_exp -c "SELECT * from master_add_node('w1', 5432);"
    $ psql -d citus_exp -c "SELECT * from master_add_node('w2', 5432);"

```

4. Verify:

```
    $ psql -d citus_exp -c "SELECT * FROM master_get_active_worker_nodes()";
```
Output:

```
 node_name | node_port
-----------+-----------
 w1        |      5432
 w2        |      5432

```



Errors
------


1. `python manage.py migrate`


```
django.db.utils.DataError: replication_factor (1) exceeds number of worker nodes (0)
HINT:  Add more worker nodes or try again with a lower replication factor.
```

2. `"SELECT create_distributed_table('ads_ads','id')"`


```
psycopg2.OperationalError: cannot create reference table "ads_ads"
DETAIL:  There are no active worker nodes.
```



3. `"SELECT create_distributed_table('ads_ads','id')"`

```
django.db.utils.ProgrammingError: cannot create foreign key constraint
DETAIL:  Referenced table must be a distributed table.

```



4. `"SELECT create_reference_table('ads_ads')"`


```
django.db.utils.NotSupportedError: cannot create foreign key constraint because reference tables are not supported as the referencing table of a foreign constraint
DETAIL:  Reference tables are only supported as the referenced table of a foreign key when the referencing table is a hash distributed table

```

https://github.com/citusdata/citus/issues/2378

Currently Citus supports foreign keys in two cases;

    From hash distributed tables to hash distributed tables when the foreign key includes the distribution column,
    From hash distributed tables to reference tables on any column.

5. `"SELECT create_distributed_table('ads_campaign', 'company_id')"`

django.db.utils.NotSupportedError: cannot create constraint on "ads_campaign"
DETAIL:  Distributed relations cannot have UNIQUE, EXCLUDE, or PRIMARY KEY constraints that do not include the partition column (with an equality operator if EXCLUDE).

