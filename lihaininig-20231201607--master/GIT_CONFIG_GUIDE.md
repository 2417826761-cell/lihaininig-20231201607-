# Git配置指南

## 配置Git用户信息

在命令行中执行以下命令（需要重启终端使Git命令生效）：

```bash
git config --global user.name "2417826761"
git config --global user.email "2417826761@qq.com"
```

## 初始化本地仓库

1. 打开命令行，进入项目目录：
   ```bash
   cd myproject
   ```

2. 初始化Git仓库：
   ```bash
   git init
   ```

3. 添加所有文件到暂存区：
   ```bash
   git add .
   ```

4. 提交初始代码：
   ```bash
   git commit -m "初始提交：完成基本功能开发"
   ```

## 创建GitHub远程仓库

1. 登录GitHub账户
2. 点击右上角"+"图标，选择"New repository"
3. 填写仓库名称（例如"django-project"）
4. 添加描述（可选）
5. 选择仓库可见性（公开或私有）
6. 不要勾选"Initialize this repository with a README"
7. 点击"Create repository"

## 连接并推送到GitHub

1. 添加远程仓库：
   ```bash
   git remote add origin https://github.com/2417826761/django-project.git
   ```
   （将URL替换为您的GitHub仓库URL）

2. 推送代码到GitHub：
   ```bash
   git push -u origin main
   ```

## 常用Git命令

- 查看状态：`git status`
- 查看提交历史：`git log`
- 创建新分支：`git checkout -b 分支名称`
- 切换分支：`git checkout 分支名称`
- 合并分支：`git merge 分支名称`
- 拉取更新：`git pull`