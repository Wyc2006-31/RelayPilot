"""温度转换命令行工具（CLI）。

复用 temperature_converter 中的纯函数完成命令行换算，
不重写任何转换公式。

用法：
    python temperature_cli.py --from c --value 100              # 摄氏 → 华氏
    python temperature_cli.py --from f --value 212              # 华氏 → 摄氏
    python temperature_cli.py --from c --value 100 --to f       # 显式指定目标单位

成功时 stdout 仅输出一行转换结果（float）；
非法 --from/--to 或非数值 --value 时以非零退出码结束，错误写 stderr。
"""

import argparse
import sys

from temperature_converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
)

# 单位别名归一：小写别名 -> 规范单位（c/f）
_UNIT_ALIASES = {
    "c": "c",
    "celsius": "c",
    "f": "f",
    "fahrenheit": "f",
}


def _normalize_unit(value):
    """将 --from/--to 取值归一为 'c' 或 'f'，无对应别名返回 None。"""
    return _UNIT_ALIASES.get((value or "").lower())


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="temperature_cli.py",
        description="温度单位换算命令行工具（摄氏 <-> 华氏）。",
    )
    parser.add_argument(
        "--from",
        dest="from_unit",
        required=True,
        help="源单位：c|celsius（摄氏→华氏）或 f|fahrenheit（华氏→摄氏）",
    )
    parser.add_argument(
        "--value",
        required=True,
        help="待转换的数值",
    )
    parser.add_argument(
        "--to",
        dest="to_unit",
        default=None,
        choices=["c", "celsius", "f", "fahrenheit"],
        help="目标单位（可选）：c|celsius|f|fahrenheit；省略时按 --from 默认方向换算",
    )
    args = parser.parse_args(argv)

    # 源单位校验（沿用既有非零退出 + stderr 语义）
    from_norm = _normalize_unit(args.from_unit)
    if from_norm is None:
        sys.stderr.write(
            "错误：非法的 --from 取值 '%s'，应为 c|celsius 或 f|fahrenheit\n"
            % args.from_unit
        )
        return 2

    try:
        value = float(args.value)
    except (ValueError, TypeError):
        sys.stderr.write(
            "错误：非数值 --value '%s'，无法转换为数字\n" % args.value
        )
        return 2

    if args.to_unit is None:
        # 省略 --to：严格保持 MINI-003 默认行为
        convert = (
            celsius_to_fahrenheit if from_norm == "c" else fahrenheit_to_celsius
        )
        result = convert(value)
    else:
        # 显式 --to：按 from/to 组合选择方向；同单位输出原值
        to_norm = _normalize_unit(args.to_unit)  # choices 已约束，必定非 None
        if from_norm == to_norm:
            result = value
        elif from_norm == "c" and to_norm == "f":
            result = celsius_to_fahrenheit(value)
        elif from_norm == "f" and to_norm == "c":
            result = fahrenheit_to_celsius(value)
        else:
            # 兜底防御（正常不可达，choices 已拦截）：非同单位且非 c<->f
            sys.stderr.write(
                "错误：不支持的换算方向 %s -> %s\n"
                % (args.from_unit, args.to_unit)
            )
            return 2

    sys.stdout.write("%s\n" % result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
