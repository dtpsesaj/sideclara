import redis
#redis_cnx = redis.Redis(host='192.168.156.3',db=1,port=6379)
redis_cnx = redis.Redis(host='127.0.0.1',db=1,port=6379)
redis_cnx.delete('declaracion')
exit()



