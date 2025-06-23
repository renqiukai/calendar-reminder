from ics import Calendar, Event
from datetime import datetime, timedelta

# 创建日历对象
calendar = Calendar()

# 设置提醒时间（每天 9 点）
start_time = datetime.utcnow().replace(hour=1, minute=0, second=0, microsecond=0)
end_time = start_time + timedelta(minutes=30)

# 定义提醒内容
summary = "📋 每日工作提醒"
description = """查看项目进度与未完成事项：
- 跟进选图项目付款状态
- 网络学院项目主功能开发安排
- 查看每日博士项目合同是否签署

📅 记得写今日日志，安排明日计划"""

# 创建事件
event = Event()
event.name = summary
event.begin = start_time
event.end = end_time
event.description = description

# 加入日历
calendar.events.add(event)

# 写入文件
with open("reminder.ics", "w", encoding="utf-8") as f:
    f.writelines(calendar)