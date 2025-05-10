# Docker容器管理系统

这是一个用于集中管理多个Docker容器的系统，支持一键启动/停止所有容器，并提供本地调试功能。系统基于Docker Compose构建，适合管理多个运行简单Python代码的容器。

## 系统结构

```
.
├── app1/                 # 应用1目录
│   ├── Dockerfile        # 应用1的Docker配置
│   ├── app.py            # 应用1的Python代码
│   └── requirements.txt  # 应用1的依赖
├── app2/                  # 应用2目录
│   ├── Dockerfile        # 应用2的Docker配置
│   ├── app.py            # 应用2的Python代码
│   └── requirements.txt  # 应用2的依赖
├── app3/                  # 应用3目录
│   ├── Dockerfile        # 应用3的Docker配置
│   ├── app.py            # 应用3的Python代码
│   └── requirements.txt  # 应用3的依赖
├── docker-compose.yml     # Docker Compose配置文件
├── manage.py              # 容器管理脚本
└── README.md              # 说明文档
```

## 前提条件

- 安装Docker：[Docker官方安装指南](https://docs.docker.com/get-docker/)
- 安装Docker Compose：[Docker Compose安装指南](https://docs.docker.com/compose/install/)
- 安装Python 3.11

## 使用方法

### 1. 构建容器

```bash
python manage.py build
```

### 2. 启动所有容器

```bash
python manage.py start
```

### 3. 查看容器状态

```bash
python manage.py status
```

### 4. 查看容器日志

```bash
python manage.py logs
```

按 `Ctrl+C` 退出日志查看。

### 5. 进入容器调试

```bash
python manage.py debug app1  # 进入app1容器
python manage.py debug app2  # 进入app2容器
python manage.py debug app3  # 进入app3容器
```

### 6. 停止所有容器

```bash
python manage.py stop
```

### 7. 查看帮助

```bash
python manage.py help
```

## 本地开发与调试

系统通过卷挂载（volumes）支持本地开发和调试。您可以直接在本地修改各应用目录下的代码，修改会实时同步到容器中，无需重新构建容器。

例如，您可以：

1. 修改 `app1/app.py` 文件
2. 保存文件后，容器内的应用会自动使用最新代码

如果您添加了新的依赖，需要在相应的 `requirements.txt` 文件中添加依赖，然后重新构建容器：

```bash
python manage.py build
python manage.py start
```

## 自定义应用

您可以根据需要修改现有应用或添加新的应用：

1. 创建新的应用目录（例如 `app4`）
2. 添加必要的文件（`Dockerfile`、`app.py`、`requirements.txt`）
3. 在 `docker-compose.yml` 中添加新服务

## 注意事项

- 确保Docker和Docker Compose已正确安装
- 如果遇到权限问题，可能需要使用管理员权限运行命令
- 在Windows系统中，可能需要调整Docker Desktop的设置以启用卷挂载功能
