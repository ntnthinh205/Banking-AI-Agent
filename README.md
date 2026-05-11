# Xây dựng hệ thống Banking AI-Agent

## 🎯 Mục tiêu tổng quan
Dự án này triển khai một **Agentic Workflow** (Luồng làm việc tác tử) tiên tiến cho hệ thống hỗ trợ khách hàng ngân hàng. Mục tiêu là tự động hóa việc xử lý các yêu cầu của khách hàng bằng cách định tuyến chúng qua một chuỗi các node thông minh. Hệ thống được thiết kế để hiểu ý định của khách hàng, đánh giá mức độ khẩn cấp của yêu cầu, truy xuất các chính sách ngân hàng liên quan, tạo ra câu trả lời nháp bằng AI, kiểm tra tính hợp lệ của câu trả lời, và cuối cùng quyết định xem có nên trả lời tự động hay chuyển tiếp vấn đề cho nhân viên hỗ trợ (con người) hay không.

Dự án này là một phần của môn học "Ứng dụng xử lý ngôn ngữ tự nhiên trong doanh nghiệp" (Applications of Natural Language Processing in Industry).

## 🔄 Kiến trúc Workflow (Luồng xử lý)
Hệ thống hoạt động dưới dạng một luồng xử lý có cấu trúc bao gồm các node bắt buộc sau:

1. **🧠 Intent Detection Node (Node Nhận diện Ý định)**: Tiếp nhận tin nhắn của khách hàng và dự đoán ý định (ví dụ: `card_not_received`, `lost_card`) sử dụng một mô hình đã được fine-tune triển khai qua gRPC.
2. **⚠️ Priority / Risk Detection Node (Node Đánh giá Mức độ Ưu tiên / Rủi ro)**: Phân loại vấn đề thành mức độ ưu tiên `Low` (Thấp), `Medium` (Trung bình), hoặc `High` (Cao) dựa trên ý định đã nhận diện và các từ khóa (ví dụ: mất tiền hoặc khóa tài khoản là ưu tiên cao).
3. **📚 Policy Retrieval Node (Node Truy xuất Chính sách)**: Lấy các đoạn FAQ, chính sách hoặc hướng dẫn hỗ trợ liên quan từ cơ sở dữ liệu giả lập (mock database) dựa trên ý định.
4. **✍️ Response Drafting Node (Node Tạo Bản nháp)**: Gọi một Mô hình Ngôn ngữ Lớn (LLM - ví dụ `gpt-oss` thông qua Ollama) để tạo ra một bản nháp câu trả lời hữu ích, được tinh chỉnh theo ngữ cảnh của khách hàng, ý định và chính sách đã truy xuất.
5. **✅ Validation Node (Node Kiểm tra Tính hợp lệ)**: Đánh giá bản nháp câu trả lời để đảm bảo tính nhất quán với chính sách và kiểm tra xem có thông tin quan trọng nào bị thiếu hay không.
6. **🚦 Routing & Escalation Node (Node Định tuyến & Chuyển tiếp)**: Đưa ra quyết định cuối cùng dựa trên mức độ ưu tiên và trạng thái hợp lệ để:
   - `reply_directly`: Gửi trực tiếp câu trả lời của AI cho người dùng.
   - `ask_info`: Yêu cầu cung cấp thêm thông tin chi tiết.
   - `escalate`: Chuyển tiếp ca xử lý cho nhân viên hỗ trợ (ví dụ: đối với mức độ ưu tiên Cao hoặc bản nháp không hợp lệ).

## 📂 Cấu trúc thư mục (Project Structure)
Dưới đây là cấu trúc mã nguồn của dự án và chức năng của từng thành phần:

```text
BT03/
├── app/
│   ├── agent/
│   │   └── orchestrator.py    # Bộ điều khiển chính của Workflow, gọi các Node theo thứ tự.
│   ├── clients/
│   │   ├── base.py            # Interface cơ sở cho việc gọi model.
│   │   └── ollama_client.py   # Client xử lý việc giao tiếp với Ollama (LLM).
│   ├── core/
│   │   ├── schemas.py         # Định nghĩa các schema (Pydantic) cho Input/Output và lưu vết (trace).
│   │   └── settings.py        # Lưu trữ các cấu hình và URL kết nối (đọc từ .env).
│   ├── data/
│   │   └── policies.py        # Lưu trữ dữ liệu giả lập (mock data) về FAQ và chính sách.
│   ├── nodes/
│   │   ├── draft_node.py      # Node sinh ra bản nháp câu trả lời sử dụng LLM.
│   │   ├── intent_node.py     # Node nhận diện ý định (Intent) sử dụng gRPC gọi mô hình từ Lab 2.
│   │   ├── policy_node.py     # Node truy xuất chính sách hỗ trợ dựa vào ý định.
│   │   ├── priority_node.py   # Node phân loại mức độ ưu tiên (Low/Medium/High).
│   │   ├── router_node.py     # Node định tuyến đưa ra quyết định xử lý cuối cùng.
│   │   └── validation_node.py # Node kiểm tra tính hợp lệ của bản nháp do AI tạo ra.
│   └── main.py                # Khởi tạo và cấu hình ứng dụng FastAPI, định nghĩa API routes.
├── examples/
│   └── sample_requests.json   # Tập tin chứa các tin nhắn mẫu của khách hàng để kiểm thử.
├── requirements.txt           # Danh sách các thư viện Python cần cài đặt.
├── run.py                     # Entry point khởi động server FastAPI.
└── README.md                  # Tài liệu hướng dẫn của dự án (file này).
```

## 🚀 Cài đặt & Chạy ứng dụng

### 1. Yêu cầu hệ thống (Prerequisites)
Đảm bảo bạn đã cài đặt Python 3.9+. Clone repository này về máy của bạn.

### 2. Cài đặt thư viện (Install Dependencies)
```bash
pip install -r requirements.txt
```

### 3. Thiết lập Môi trường (Environment Setup)
Hệ thống phụ thuộc vào các mô hình bên ngoài để nhận diện Intent và sinh văn bản LLM (Ollama). Đảm bảo bạn đã cấu hình file `.env` ở thư mục gốc. Nếu bạn đang sử dụng Google Colab kết hợp với Pinggy tunnels, file `.env` của bạn sẽ trông giống như sau:

```env
# Ví dụ cấu hình .env
INTENT_GRPC_TARGET=your-intent-model-tunnel.pinggy.link
OLLAMA_BASE_URL=http://your-ollama-tunnel.pinggy.link
OLLAMA_MODEL=gpt-oss-20b # Hoặc mô hình bạn đã chọn
```

### 4. Chạy ứng dụng (Running the Application)
Dự án sử dụng **FastAPI** để phục vụ Agentic Workflow.
Để khởi động server, hãy chạy lệnh:
```bash
python run.py
```
Sau khi server chạy, bạn có thể xem tài liệu API tương tác (Swagger UI) tại:
👉 **http://localhost:8000/docs**

### 5. Kiểm thử bằng các câu mẫu (Testing)
Bạn có thể kiểm thử hệ thống bằng các câu hỏi mẫu được cung cấp trong file `examples/sample_requests.json` thông qua giao diện Swagger UI tại đường dẫn `/docs`.

## 🎥 Video Demo
[Chèn đường link Video của bạn vào đây]

---
