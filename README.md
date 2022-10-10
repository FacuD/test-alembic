## Initialize alembic

1. `alembic init alembic`
2. Change the `sqlalchemy.url` variable inside the `alembic.ini` file to the database url
3. Run `alembic revision -m "create account table"` to create a new revision
4. Change the upgrade and downgrade functions inside the newly created revision file with your desired changes
5. Run `alembic upgrade head` to apply the changes to the database

## Tips:

1. You can do `alembic downgrade -1` to undo the last change or `alembic upgrade +1` to redo the last change
2. You can see all the commits with `alembic history --verbose`
3. You can see the current revision with `alembic current`
4. Yoy can downgrade to base with `alembic downgrade base` or upgrade to head with `alembic upgrade head`

## PS:

If u want to use this in production, you should change `sqlalchemy.url` (inside alembic.ini) to a variable and set it in some .ini/.env file. Something like this: `sqlalchemy.url = ${DATABASE_URL}`

### Happy coding! :D
