"""
汇率监控工具配置文件
"""

# 飞书消息发送配置（两种方式，选择其一）

# 方式1：飞书自定义机器人Webhook（推荐，简单快捷）
# 在飞书群组中添加"自定义机器人"，复制Webhook地址填入下方
FEISHU_WEBHOOK_URL = "https://open.feishu.cn/open-apis/bot/v2/hook/ff6c5467-2514-4c60-ad6b-0899fb1828ca"

# 方式2：飞书开放平台应用（需要激活机器人能力）
# 如果使用此方式，需要在飞书开放平台创建应用并启用机器人功能
FEISHU_APP_ID = "cli_a92bd1539df91bdb"
FEISHU_APP_SECRET = "0qq2mnyudMGdX68iOHGOHfvZ8mlLvMCG"
RECIPIENT_EMAIL = "gloria.yang@anker.com"

# 汇率API配置
# 使用ExchangeRate-API（免费版）：https://www.exchangerate-api.com/
# 注册后获取API密钥，免费额度1500次/月
EXCHANGE_RATE_API_KEY = "d8d2fa00ef7de06ed4c98d3c"
EXCHANGE_RATE_API_URL = "https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"

# 需要监控的汇率对
CURRENCY_PAIRS = [
    {"base": "USD", "target": "JPY", "name": "美元对日元"},
    {"base": "CNY", "target": "JPY", "name": "人民币对日元"},
    {"base": "USD", "target": "CNY", "name": "美元对人民币"},
    {"base": "USD", "target": "KRW", "name": "美元对韩元"}
]

# 定时任务配置
SCHEDULE_TIME = "09:00"  # 每天9点执行

# 日志配置
LOG_FILE = "exchange_rate_monitor.log"
