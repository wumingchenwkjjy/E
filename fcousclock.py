import time
import datetime

total_time = 60 * 60 # 1小时

start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(seconds=total_time)

print("专注时钟开始,总计时长为:{}小时".format(total_time//3600))

while datetime.datetime.now() < end_time:
    time.sleep(1)
    remaining = end_time - datetime.datetime.now()
    print("\r专注倒计时:{}分{}秒".format(remaining.seconds//60, remaining.seconds%60), end="")
    
print("\n专注时钟结束!")
