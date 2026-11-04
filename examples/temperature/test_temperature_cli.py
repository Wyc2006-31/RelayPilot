"""temperature_cli.py 的集成测试（标准库 unittest + subprocess）。

通过子进程调用：
    python temperature_cli.py --from <unit> --value <val>
cwd 固定为本测试文件所在目录；数值用近似相等（容差 1e-6）。
"""

import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
TOL = 1e-6


def run_cli(args):
    """以 cwd=HERE 启动 temperature_cli.py，返回 CompletedProcess。"""
    return subprocess.run(
        [sys.executable, "temperature_cli.py"] + list(args),
        cwd=HERE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )


class TestCLISuccess(unittest.TestCase):
    # 1. 摄氏 -> 华氏
    def test_c_to_f_zero(self):
        proc = run_cli(["--from", "c", "--value", "0"])
        self.assertEqual(proc.returncode, 0)
        out = proc.stdout.rstrip("\n")
        self.assertEqual(len(out.splitlines()), 1)
        self.assertAlmostEqual(float(out), 32.0, delta=TOL)

    def test_c_to_f_boiling(self):
        proc = run_cli(["--from", "c", "--value", "100"])
        self.assertEqual(proc.returncode, 0)
        out = proc.stdout.rstrip("\n")
        self.assertEqual(len(out.splitlines()), 1)
        self.assertAlmostEqual(float(out), 212.0, delta=TOL)

    # 2. 华氏 -> 摄氏
    def test_f_to_c_freezing(self):
        proc = run_cli(["--from", "f", "--value", "32"])
        self.assertEqual(proc.returncode, 0)
        out = proc.stdout.rstrip("\n")
        self.assertEqual(len(out.splitlines()), 1)
        self.assertAlmostEqual(float(out), 0.0, delta=TOL)

    def test_f_to_c_boiling(self):
        proc = run_cli(["--from", "f", "--value", "212"])
        self.assertEqual(proc.returncode, 0)
        out = proc.stdout.rstrip("\n")
        self.assertEqual(len(out.splitlines()), 1)
        self.assertAlmostEqual(float(out), 100.0, delta=TOL)

    # 3. 别名
    def test_alias_celsius(self):
        proc = run_cli(["--from", "celsius", "--value", "100"])
        self.assertEqual(proc.returncode, 0)
        out = proc.stdout.rstrip("\n")
        self.assertEqual(len(out.splitlines()), 1)
        self.assertAlmostEqual(float(out), 212.0, delta=TOL)

    def test_alias_fahrenheit(self):
        proc = run_cli(["--from", "fahrenheit", "--value", "32"])
        self.assertEqual(proc.returncode, 0)
        out = proc.stdout.rstrip("\n")
        self.assertEqual(len(out.splitlines()), 1)
        self.assertAlmostEqual(float(out), 0.0, delta=TOL)


class TestCLIFailure(unittest.TestCase):
    # 4. 非法 --from
    def test_invalid_from(self):
        proc = run_cli(["--from", "k", "--value", "1"])
        self.assertNotEqual(proc.returncode, 0)
        self.assertTrue(proc.stderr.strip() != "")

    # 5. 非数值 --value
    def test_nonnumeric_value(self):
        proc = run_cli(["--from", "c", "--value", "abc"])
        self.assertNotEqual(proc.returncode, 0)
        self.assertTrue(proc.stderr.strip() != "")

    # 6. 缺必填
    def test_missing_from(self):
        proc = run_cli(["--value", "10"])
        self.assertNotEqual(proc.returncode, 0)

    def test_missing_value(self):
        proc = run_cli(["--from", "c"])
        self.assertNotEqual(proc.returncode, 0)

    def test_no_args(self):
        proc = run_cli([])
        self.assertNotEqual(proc.returncode, 0)


class TestCLIBehavior(unittest.TestCase):
    # 7. 成功：stdout 单行可解析 float 且 exit 0
    def test_success_stdout_single_line_float_exit_zero(self):
        proc = run_cli(["--from", "c", "--value", "25"])
        self.assertEqual(proc.returncode, 0)
        out = proc.stdout.rstrip("\n")
        self.assertEqual(len(out.splitlines()), 1)
        parsed = float(out)  # 必须可解析为 float
        self.assertAlmostEqual(parsed, 77.0, delta=TOL)

    # 7. 失败：exit 非 0（覆盖所有失败分支）
    def test_failure_exit_nonzero(self):
        failure_cases = [
            ["--from", "k", "--value", "1"],          # 非法 --from
            ["--from", "c", "--value", "abc"],        # 非数值 --value
            ["--value", "10"],                         # 缺 --from
            ["--from", "c"],                           # 缺 --value
            [],                                         # 完全无参数
        ]
        for args in failure_cases:
            with self.subTest(args=args):
                proc = run_cli(args)
                self.assertNotEqual(proc.returncode, 0)


class TestCLITargetUnit(unittest.TestCase):
    # 默认路径回归（省略 --to 必须与 MINI-003 旧行为完全一致）
    def test_default_regression_c_to_f(self):
        proc = run_cli(["--from", "c", "--value", "100"])
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(proc.stderr.strip(), "")
        self.assertEqual(proc.stdout.strip(), "212.0")

    def test_default_regression_f_to_c(self):
        proc = run_cli(["--from", "f", "--value", "32"])
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout.strip(), "0.0")

    # 显式 --to 正向路径
    def test_explicit_to_f(self):
        proc = run_cli(["--from", "c", "--value", "100", "--to", "f"])
        self.assertEqual(proc.returncode, 0)
        out = proc.stdout.rstrip("\n")
        self.assertEqual(len(out.splitlines()), 1)
        self.assertEqual(out, "212.0")

    def test_explicit_to_c(self):
        proc = run_cli(["--from", "f", "--value", "32", "--to", "c"])
        self.assertEqual(proc.returncode, 0)
        out = proc.stdout.rstrip("\n")
        self.assertEqual(len(out.splitlines()), 1)
        self.assertEqual(out, "0.0")

    def test_explicit_to_f_zero(self):
        proc = run_cli(["--from", "c", "--value", "0", "--to", "f"])
        self.assertEqual(proc.returncode, 0)
        out = proc.stdout.rstrip("\n")
        self.assertEqual(len(out.splitlines()), 1)
        self.assertEqual(out, "32.0")

    # 同单位恒等路径
    def test_identity_c(self):
        proc = run_cli(["--from", "c", "--value", "100", "--to", "c"])
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout.strip(), "100.0")

    def test_identity_f(self):
        proc = run_cli(["--from", "f", "--value", "-40", "--to", "f"])
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout.strip(), "-40.0")

    # 长名别名路径
    def test_alias_long_c_to_f(self):
        proc = run_cli(["--from", "celsius", "--value", "100", "--to", "fahrenheit"])
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout.strip(), "212.0")

    def test_alias_long_f_to_c(self):
        proc = run_cli(["--from", "fahrenheit", "--value", "212", "--to", "celsius"])
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout.strip(), "100.0")

    # 失败路径：非法 --to 必须经 argparse invalid choice 非零退出
    def test_invalid_to(self):
        proc = run_cli(["--from", "c", "--value", "100", "--to", "k"])
        self.assertNotEqual(proc.returncode, 0)
        self.assertTrue(proc.stdout.strip() == "" or "212.0" not in proc.stdout)
        self.assertTrue(proc.stderr.strip() != "")
        self.assertIn("invalid choice", proc.stderr.lower())

    # 失败路径：非数值 --value 与 --to 同时存在
    def test_nonnumeric_value_with_to(self):
        proc = run_cli(["--from", "c", "--value", "abc", "--to", "f"])
        self.assertNotEqual(proc.returncode, 0)
        self.assertTrue(proc.stderr.strip() != "")


if __name__ == "__main__":
    unittest.main()
