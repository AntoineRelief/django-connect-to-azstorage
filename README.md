https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-file-datalake/samples

# Start

Create a `.env` file. Add two credentials:
```
STORAGE_ACCOUNT_NAME=
STORAGE_ACCOUNT_KEY=
```

The keys should come from a Storage account.

```
docker-compose up --build
docker-compose run web python manage.py migrate
docker-compose run web puthon manage.py createsuperuser
```

Create a first item, going to `http://localhost:8000/api/blocks`

In the Storage account, create a container named `block1`.

In the new container, create a file called `1.json`, with this content:

```json
{
  "name": "test"
}
```

Try the route:
`http://localhost:8000/api/dl-blocks/1/`

You should get a result from the data lake.