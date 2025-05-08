#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

def print_header(message):
    print("\n" + "=" * 50)
    print(message)
    print("=" * 50)

def start_containers():
    print_header("启动所有容器")
    subprocess.run(["docker-compose", "up", "-d"], check=True)
    print("所有容器已成功启动！")

def stop_containers():
    print_header("停止所有容器")
    subprocess.run(["docker-compose", "down"], check=True)
    print("所有容器已成功停止！")

def build_containers():
    print_header("构建所有容器")
    subprocess.run(["docker-compose", "build"], check=True)
    print("所有容器已成功构建！")

def show_logs():
    print_header("显示容器日志")
    try:
        subprocess.run(["docker-compose", "logs", "--follow"], check=False)
    except KeyboardInterrupt:
        print("\n已退出日志查看")

def show_status():
    print_header("容器状态")
    subprocess.run(["docker-compose", "ps"], check=True)

def debug_container(container_name):
    print_header(f"进入{container_name}容器进行调试")
    try:
        subprocess.run(["docker-compose", "exec", container_name, "bash"], check=False)
    except:
        try:
            # 如果bash不可用，尝试使用sh
            subprocess.run(["docker-compose", "exec", container_name, "sh"], check=False)
        except:
            print(f"无法进入{container_name}容器进行调试")

def show_help():
    print_header("Docker容器管理系统帮助")
    print("使用方法: python manage.py [命令]")
    print("\n可用命令:")
    print("  start       - 启动所有容器")
    print("  stop        - 停止所有容器")
    print("  build       - 构建所有容器")
    print("  logs        - 查看容器日志")
    print("  status      - 查看容器状态")
    print("  debug [容器名] - 进入指定容器进行调试")
    print("  help        - 显示帮助信息")

def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "start":
        start_containers()
    elif command == "stop":
        stop_containers()
    elif command == "build":
        build_containers()
    elif command == "logs":
        show_logs()
    elif command == "status":
        show_status()
    elif command == "debug" and len(sys.argv) > 2:
        debug_container(sys.argv[2])
    elif command == "help":
        show_help()
    else:
        print("未知命令，请使用 'python manage.py help' 查看帮助")

if __name__ == "__main__":
    main()