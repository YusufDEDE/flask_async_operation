# Flask Async Operation

> System Requirements
- redis
- python3.x


> install
```shell script
$ touch .env # look .env-example
$ pip install -r requirements
```
> run 
```shell script
$ python run.py
$ rqworker
```
---
##### usage CLI, task operation

> create --name --priority
```shell script
$ python manage.py create "System BugBounty Date" "high"
```
> lists
```shell script
$ python manage.py lists
```
> delete --id
```shell script
$ python manage.py delete 2
```