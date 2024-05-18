import redis
r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True,
)

img_keep=[]


def alpr_db():
    stored_alpr  = r.hgetall(
        "alpr_plate_to_img"
        )
    for key, value in stored_alpr.items():
        a = f"{value}."    
        #print(f"{key} has the color {value}.")
        print((a)) 
        print((a)) 

    return(stored_alpr) 

alpr_db()