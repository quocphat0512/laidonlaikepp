import streamlit as st

# Tiêu đề của ứng dụng web
st.title("Ứng dụng Tính Lãi Tiền Gửi 💰")
st.markdown("So sánh giữa **Lãi Đơn** và **Lãi Kép**")

st.divider()

# Tạo form nhập liệu
st.subheader("Nhập thông tin gửi tiền")
# Sử dụng number_input thay cho input()
a = st.number_input("Nhập số tiền khách hàng gửi (VNĐ):", min_value=0.0, step=1000000.0, format="%.2f")
b = st.number_input("Nhập số tháng khách hàng gửi:", min_value=0.0, step=1.0, format="%.0f")

# Có thể cho phép người dùng nhập lãi suất hoặc để mặc định như code gốc
c = st.number_input("Lãi suất năm (%):", value=5.0, step=0.1) / 100 

st.divider()

# Chỉ tính toán khi đã nhập số tiền và số tháng lớn hơn 0
if a > 0 and b > 0:
    # --- Tính toán ---
    tong_tien_lai_don = a * (1 + c / 12 * b)
    tong_tien_lai_kep = a * (1 + c / 12) ** b  # Đã sửa **5 thành **b
    
    # --- Hiển thị kết quả ---
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("TÍNH THEO LÃI ĐƠN")
        st.write(f"**Tổng tiền nhận được:** {tong_tien_lai_don:,.4f} VNĐ")
        st.write(f"**Tiền lãi sinh ra:** {tong_tien_lai_don - a:,.2f} VNĐ")
        
    with col2:
        st.info("TÍNH THEO LÃI KÉP")
        st.write(f"**Tổng tiền nhận được:** {tong_tien_lai_kep:,.4f} VNĐ")
        st.write(f"**Tiền lãi sinh ra:** {tong_tien_lai_kep - a:,.2f} VNĐ")
