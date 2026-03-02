"""
汇率获取模块
使用ExchangeRate-API获取实时汇率数据
"""

import requests
from typing import Dict, Optional
from datetime import datetime
import config


def get_exchange_rate(base_currency: str, target_currency: str) -> Optional[Dict]:
    """
    获取指定货币对的汇率

    Args:
        base_currency: 基础货币代码（如 USD, CNY）
        target_currency: 目标货币代码（如 JPY, KRW）

    Returns:
        包含汇率信息的字典，失败返回None
    """
    try:
        url = config.EXCHANGE_RATE_API_URL.format(
            api_key=config.EXCHANGE_RATE_API_KEY,
            base_currency=base_currency
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("result") == "success":
            rate = data["conversion_rates"].get(target_currency)
            if rate:
                return {
                    "base": base_currency,
                    "target": target_currency,
                    "rate": rate,
                    "timestamp": data.get("time_last_update_utc"),
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

        return None

    except requests.RequestException as e:
        print(f"获取汇率失败 ({base_currency}/{target_currency}): {str(e)}")
        return None
    except Exception as e:
        print(f"处理汇率数据时出错: {str(e)}")
        return None


def get_all_exchange_rates() -> list:
    """
    获取所有配置的汇率对数据

    Returns:
        汇率信息列表
    """
    rates = []

    for pair in config.CURRENCY_PAIRS:
        rate_info = get_exchange_rate(pair["base"], pair["target"])
        if rate_info:
            rate_info["name"] = pair["name"]
            rates.append(rate_info)
        else:
            print(f"警告：无法获取 {pair['name']} 的汇率")

    return rates


def format_rate_message(rates: list) -> str:
    """
    格式化汇率信息为可读的文本消息

    Args:
        rates: 汇率信息列表

    Returns:
        格式化后的消息文本
    """
    if not rates:
        return "无法获取汇率数据"

    current_date = datetime.now().strftime("%Y年%m月%d日 %H:%M")
    message_lines = [
        f"📊 每日汇率监控报告",
        f"⏰ 更新时间：{current_date}",
        "",
        "━━━━━━━━━━━━━━━━━━━━"
    ]

    for rate in rates:
        message_lines.append(f"💱 {rate['name']}")
        message_lines.append(f"   {rate['base']}/{rate['target']} = {rate['rate']:.4f}")
        message_lines.append("")

    message_lines.append("━━━━━━━━━━━━━━━━━━━━")

    return "\n".join(message_lines)
