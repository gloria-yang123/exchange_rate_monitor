"""
汇率监控主程序
每日获取汇率并发送飞书通知
"""

import sys
from datetime import datetime
from exchange_rate import get_all_exchange_rates, format_rate_message
from feishu_sender import FeishuSender
from feishu_webhook import send_rate_report_webhook
import config


def main():
    """主函数"""
    print(f"开始执行汇率监控任务 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # 1. 获取汇率数据
    print("正在获取汇率数据...")
    rates = get_all_exchange_rates()

    if not rates:
        print("错误：无法获取任何汇率数据")
        sys.exit(1)

    print(f"成功获取 {len(rates)} 组汇率数据")

    # 2. 格式化消息
    message = format_rate_message(rates)
    print("\n生成的汇率报告：")
    print(message)

    # 3. 发送飞书消息（优先使用Webhook方式）
    print("\n正在发送飞书消息...")

    # 检查是否配置了Webhook
    if hasattr(config, 'FEISHU_WEBHOOK_URL') and config.FEISHU_WEBHOOK_URL:
        print("使用Webhook方式发送...")
        success = send_rate_report_webhook(message)
    else:
        print("使用应用API方式发送...")
        sender = FeishuSender()
        success = sender.send_rate_report(message)

    if success:
        print("✓ 汇率报告发送成功")
        sys.exit(0)
    else:
        print("✗ 汇率报告发送失败")
        print("\n提示：")
        print("- 如使用Webhook方式，请在config.py中配置FEISHU_WEBHOOK_URL")
        print("- 如使用应用方式，请确保应用已激活机器人能力")
        sys.exit(1)


if __name__ == "__main__":
    main()
