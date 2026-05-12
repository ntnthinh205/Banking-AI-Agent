# 🏦 Hệ thống Hỗ trợ Khách hàng Ngân hàng (Banking AI-Agent)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a67d.svg)
![Ollama](https://img.shields.io/badge/LLM-Ollama-white.svg)

## 🎯 Mục tiêu tổng quan
Dự án này triển khai một **Agentic Workflow** tiên tiến dành cho hệ thống hỗ trợ khách hàng trong lĩnh vực ngân hàng. Hệ thống tự động hóa việc xử lý các yêu cầu của khách hàng bằng cách định tuyến thông minh qua một chuỗi các node xử lý. AI Agent được thiết kế để:
- Hiểu ý định cốt lõi của khách hàng.
- Đánh giá mức độ khẩn cấp (Priority).
- Truy xuất các chính sách/hướng dẫn ngân hàng liên quan.
- Tự động sinh ra câu trả lời nháp (Drafting) thông qua LLM.
- Kiểm tra tính hợp lệ (Validation) của câu trả lời.
- Đưa ra quyết định cuối cùng: phản hồi tự động, yêu cầu thêm thông tin, hoặc chuyển tiếp cho nhân viên hỗ trợ.

*Dự án này là một phần của môn học "Ứng dụng Xử lý Ngôn ngữ Tự nhiên trong Doanh nghiệp".*

## 🔄 Kiến trúc Workflow (Luồng xử lý)
Hệ thống hoạt động dưới dạng một luồng xử lý có cấu trúc (State-machine), bao gồm 6 node tuần tự:

1. **🧠 Intent Detection Node**: Tiếp nhận tin nhắn và nhận diện ý định (ví dụ: `card_not_received`, `lost_card`) thông qua một mô hình [fine-tune](https://github.com/ntnthinh205/finetune-banking77).
2. **⚠️ Priority / Risk Detection Node**: Phân loại mức độ rủi ro (`Low`, `Medium`, `High`) dựa trên ý định và từ khóa.
3. **📚 Policy Retrieval Node**: Tra cứu cơ sở dữ liệu giả lập để lấy các FAQ và chính sách hỗ trợ tương ứng.
4. **✍️ Response Drafting Node**: Gọi LLM (ví dụ: `gpt-oss-20b` qua Ollama) để soạn thảo câu trả lời dựa trên ngữ cảnh khách hàng và chính sách.
5. **✅ Validation Node**: Đánh giá bản nháp, đảm bảo AI không tự bịa đặt thông tin (hallucination) và bám sát chính sách.
6. **🚦 Routing & Escalation Node**: Ra quyết định định tuyến (`reply_directly`, `ask_info`, `escalate`).

## 📂 Cấu trúc mã nguồn

```text
├── app/
│   ├── agent/
│   │   └── orchestrator.py    # Bộ điều khiển chính của Workflow, gọi các Node theo thứ tự.
│   ├── clients/
│   │   ├── base.py            # Interface cơ sở cho việc gọi model.
│   │   └── ollama_client.py   # Client xử lý việc giao tiếp với Ollama.
│   ├── core/
│   │   ├── schemas.py         # Định nghĩa các schema (Pydantic) cho Input/Output.
│   │   └── settings.py        # Lưu trữ cấu hình và các biến môi trường (đọc từ .env).
│   ├── data/
│   │   └── policies.py        # Lưu trữ dữ liệu mock về FAQ và chính sách.
│   ├── nodes/
│   │   ├── draft_node.py      # Node sinh bản nháp bằng LLM.
│   │   ├── intent_node.py     # Node nhận diện Intent qua gRPC.
│   │   ├── policy_node.py     # Node truy xuất chính sách.
│   │   ├── priority_node.py   # Node phân loại mức độ ưu tiên.
│   │   ├── router_node.py     # Node định tuyến xử lý cuối cùng.
│   │   └── validation_node.py # Node kiểm tra tính hợp lệ.
│   └── main.py                # Khởi tạo ứng dụng FastAPI và định nghĩa API routes.
├── examples/
│   └── sample_requests.json   # Tập tin chứa tin nhắn mẫu của khách hàng để kiểm thử.
├── requirements.txt           # Danh sách các thư viện Python cần cài đặt.
├── run.py                     # Entry point khởi động server FastAPI.
└── README.md                  # Tài liệu hướng dẫn.
```

## 🚀 Cài đặt & Khởi chạy

### 1. Yêu cầu hệ thống
- Python 3.9 trở lên.

### 2. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### 3. Cấu hình môi trường (.env)
Tạo file `.env` tại thư mục gốc của dự án. File cấu hình mẫu (cho Google Colab + Pinggy) sẽ có dạng:
```env
INTENT_GRPC_TARGET=your-intent-model-tunnel.pinggy.link
OLLAMA_BASE_URL=http://your-ollama-tunnel.pinggy.link
OLLAMA_MODEL=gpt-oss-20b
HOST=0.0.0.0
PORT=8000
```

### 4. Chạy ứng dụng
Khởi động server FastAPI bằng lệnh:
```bash
python run.py
```
👉 Truy cập **Swagger UI** để kiểm thử API tương tác tại: `http://localhost:8000/docs` (Hoặc theo Port bạn đã set trong `.env`)

### 5. Kiểm thử
Sử dụng các câu hỏi mẫu trong file `examples/sample_requests.json` để test hệ thống thông qua Swagger UI.

## 🎥 Video Demo
▶️ **[Xem Video Demo chi tiết](https://drive.google.com/file/d/1u2EGgzwG8wOHbwgKXmhwKVxlPUgUm0hr/view?usp=sharing)**

---
*Phát triển cho môn học: Ứng dụng Xử lý Ngôn ngữ Tự nhiên trong Doanh nghiệp - Đại học Khoa học Tự nhiên.*
