**Note:** Make sure to back-up your data before any migration!!!

To create the initial migration repository:

`flask db init`

To automatically migrate your data with alembic:

`flask db migrate -m 'create user tables'`

The above command only generated the migration script. To apply the changes to the database:

`flask db upgrade`

There is also a `flask db downgrade` which undoes the last changes applied to the database.

