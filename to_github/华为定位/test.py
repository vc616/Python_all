import json
s = {
    "code": "0",
    "info": "Success.",
    "exeResult": "900",
    "executeTime": 1634024029077,
    "currentTime": 1634024088656,
    "locateInfo": "{\"accuracy\":40.0,\"batteryStatus\":\"{\\\"isCharging\\\":\\\"1\\\",\\\"percentage\\\":\\\"100\\\"}\",\"country\":\"0\",\"createTime\":-1,\"isLockScreen\":1,\"latitude\":39.799212041027296,\"latitude_WGS\":39.791744,\"longitude\":116.51219525967707,\"longitude_WGS\":116.499802,\"networkInfo\":\"{\\\"name\\\":\\\"LINK66_5G\\\",\\\"signal\\\":\\\"4\\\",\\\"type\\\":\\\"0\\\"}\",\"simInfo\":\"{\\\"no\\\":\\\"+8613466648179,+8618031238420\\\"}\",\"type\":0}",
    
    }


# print(s["locateInfo"])
s1 = json.loads(s["locateInfo"])
print(s1['latitude_WGS'])

print(s1['longitude_WGS'])
print(s1['latitude'])

print(s1['longitude'])

