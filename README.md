已为您适配 GPL-3.0 许可证的 README 文件，以下是更新后的版本：

```markdown
# 🧮 CalcSphere - Modern Scientific Calculator

[![PyPI](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![PyQt6](https://img.shields.io/badge/PyQt6-6.4.0-green)](https://www.riverbankcomputing.com/software/pyqt/)
[![License](https://img.shields.io/badge/License-GPL--3.0-red.svg)](LICENSE)

---

## 🌟 功能亮点

- **科学计算**  
  ✅ 三角函数（sin/cos/tan）  
  ✅ 对数/指数运算（log, ^）  
  ✅ 括号支持复杂表达式

- **现代 UI**  
  🌙/☀️ 实时主题切换（暗黑/浅色模式）  
  📋 计算历史记录（带点击恢复功能）  
  ⌨️ 完全键盘支持

- **智能特性**  
  🚨 自动错误处理  
  📊 响应式布局（自适应屏幕）  
  🔄 遵循数学运算优先级

---

## 📸 界面预览

![Dark Theme](assets/screenshots/dark_theme.png#gh-light-mode-only)
![Light Theme](assets/screenshots/light_theme.png#gh-dark-mode-only)

---

## 🛠️ 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行程序
```bash
python main.py
```

### 打包成独立应用
```bash
pyinstaller --onefile --windowed main.py
```

---

## 📚 技术栈

| 组件         | 技术选型                | 作用                     |
|--------------|-------------------------|--------------------------|
| 核心框架     | PyQt6                   | 构建桌面级GUI            |
| 计算引擎     | numexpr                 | 安全计算数学表达式       |
| 样式系统     | QSS (Qt Style Sheets)   | 实现主题切换             |
| 历史管理     | JSON 文件存储           | 本地持久化记录           |

---

## 🧪 测试覆盖

```bash
# 运行单元测试
pytest tests/
```

测试模块包含：
- 计算逻辑验证 (`test_model.py`)
- UI 交互测试 (`test_ui.py`)

---

## 📄 项目结构
```markdown
calculator-app/
├── app/              # 核心代码
│   ├── model.py      # 计算逻辑
│   ├── view.py       # UI 布局
│   └── controller.py # 业务逻辑
├── assets/           # 静态资源
│   ├── styles/       # 主题样式表
│   └── icons/        # 界面图标
└── main.py           # 入口文件
```

---

## 🤝 如何贡献

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

> ⚠️ 根据 GPL-3.0 协议，任何衍生作品必须保持相同许可证

---

## 📜 许可证

本项目采用 [GNU General Public License v3.0](LICENSE)，您可以在以下条件下使用本项目：
- 💡 自由使用、修改和分发
- 🔍 必须公开修改后的源代码
- 🔄 衍生作品必须采用相同许可证

```text
CalcSphere - Modern Scientific Calculator
Copyright (C) 2023 Your Name

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
```
```
