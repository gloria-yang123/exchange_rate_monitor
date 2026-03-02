"""
飞书Webhook消息发送模块（使用自定义机器人）
更简单的方案，不需要复杂的权限配置
"""

import requests
from typing import Optional
import config


def send_webhook_message(webhook_url: str, message: str) -> bool:
    """
    通过Webhook发送消息到飞书群组

    Args:
        webhook_url: 飞书自定义机器人的Webhook URL
        message: 消息内容

    Returns:
        发送成功返回True，否则返回False
    """
    payload = {
        "msg_type": "text",
        "content": {
            "text": message
        }
    }

    try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("code") == 0:
            print("消息发送成功")
            return True
        else:
            print(f"消息发送失败: {data.get('msg')}")
            return False

    except Exception as e:
        print(f"发送消息异常: {str(e)}")
        return False


def send_rate_report_webhook(message: str) -> bool:
    """
    发送汇率报告（使用Webhook方式）

    Args:
        message: 汇率报告消息内容

    Returns:
        发送成功返回True，否则返回False
    """
    if not hasattr(config, 'FEISHU_WEBHOOK_URL') or not config.FEISHU_WEBHOOK_URL:
        print("错误：未配置FEISHU_WEBHOOK_URL")
        return False

    return send_webhook_message(config.FEISHU_WEBHOOK_URL, message)
