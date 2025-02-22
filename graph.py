import streamlit as st
import re
import pandas as pd
import plotly.express as px

df = pd.read_csv("score.csv", low_memory=False)
st.title('BẢNG ĐIỂM LỚP PY4AI 09/2022')


def sohs():
    def xulyfile():
        df['S1'].fillna(0, inplace=True)
        df['S2'].fillna(0, inplace=True)
        df['S3'].fillna(0, inplace=True)
        df['S4'].fillna(0, inplace=True)
        df['S5'].fillna(0, inplace=True)
        df['S6'].fillna(0, inplace=True)
        df['S7'].fillna(0, inplace=True)
        df['S8'].fillna(0, inplace=True)
        df['S9'].fillna(0, inplace=True)
        df['S10'].fillna(0, inplace=True)
        df['BONUS'].fillna(0, inplace=True)
        df['REG-MC4AI'].fillna('N', inplace=True)

    st.write('BIỂU ĐỒ MÔ TẢ SỐ LƯỢNG HỌC SINH NAM VÀ NỮ')
    st.plotly_chart(px.pie(df, names = 'GENDER'))
    st.write('Kết luận: ')

    def khoi(row):
        if row['CLASS'].startswith('10'):
            return 'Khối 10'
        else:
            return 'Khối 11 và 12'
    df['KHỐI'] = df.apply(khoi, axis=1)
    st.write('BIỂU ĐỒ MÔ TẢ SỐ HỌC SINH KHỐI 10 VÀ HỌC SINH HAI KHỐI CÒN LẠI')
    st.plotly_chart(px.pie(df, names = 'KHỐI'))
    st.write('Kết luận: ')

    def cg(row):
        if re.search('..CV.', row['CLASS']):
            return 'Chuyên Văn'
        elif re.search('..CT.$', row['CLASS']):
            return 'Chuyên Toán'
        elif re.search('..CL.', row['CLASS']):
            return 'Chuyên Lý'
        elif re.search('..CH.', row['CLASS']):
            return 'Chuyên Hoá'
        elif re.search('..CA.', row['CLASS']):
            return 'Chuyên Anh'
        elif re.search('..CTIN', row['CLASS']):
            return 'Chuyên Tin'
        elif re.search('..CTRN', row['CLASS']):
            return 'Chuyên Trung Nhật'
        elif re.search('..CSD', row['CLASS']):
            return 'Chuyên Sử Địa'
        elif re.search('..TH.', row['CLASS']) or re.search('..SN', row['CLASS']):
            return 'Tích Hợp/Song Ngữ'
        else:
            return 'Khác'
    df['CLASS_GROUP'] = df.apply(cg, axis=1)
    st.write('BIỂU ĐỒ MÔ TẢ SỐ HỌC SINH Ở CÁC LỚP CHUYÊN')
    st.plotly_chart(px.pie(df, names = 'CLASS_GROUP'))
    st.write('Kết luận: ')

    def ca(row):
        if row['PYTHON-CLASS'].endswith('S'):
            return 'SÁNG'
        else:
            return 'CHIỀU'
    df['CA HỌC'] = df.apply(ca, axis=1)
    st.write('BIỂU ĐỒ MÔ TẢ SỐ HỌC SINH CHỌN CA HỌC')
    st.plotly_chart(px.pie(df, names = 'CA HỌC'))
    st.write('Kết luận: ')
    
    def pf(row):
        if row['GPA'] >= 6:
            return 'Pass'
        else:
            return 'Fail'
    df['Pass/Fail'] = df.apply(pf, axis=1)
    st.write('BIỂU ĐỒ MÔ TẢ SỐ HỌC SINH ĐẬU LÊN LỚP MC')
    st.plotly_chart(px.pie(df, names = 'Pass/Fail'))
    st.write('Kết luận: ')

    st.write('BIỂU ĐỒ MÔ TẢ SỐ HỌC SINH ĐĂNG KÍ HỌC TIẾP LỚP MC4AI')
    st.plotly_chart(px.pie(df, names = 'REG-MC4AI'))
    st.write('Kết luận: ')
sohs()

def cgag(df):
    if re.search('..CV.', df['CLASS']) and df['GENDER'] == 'F':
        return 'Nữ Chuyên Văn'
    elif re.search('..CV.', df['CLASS']) and df['GENDER'] == 'M':
        return 'Nam Chuyên Văn'
    elif re.search('..CT.$', df['CLASS']) and df['GENDER'] == 'F':
        return 'Nữ Chuyên Toán'
    elif re.search('..CT.$', df['CLASS']) and df['GENDER'] == 'M':
        return 'Nam Chuyên Toán'
    elif re.search('..CL.', df['CLASS']) and df['GENDER'] == 'F':
        return 'Nữ Chuyên Lý'
    elif re.search('..CL.', df['CLASS']) and df['GENDER'] == 'M':
        return 'Nam Chuyên Lý'
    elif re.search('..CH.', df['CLASS']) and df['GENDER'] == 'F':
        return 'Nữ Chuyên Hoá'
    elif re.search('..CH.', df['CLASS']) and df['GENDER'] == 'M':
        return 'Nam Chuyên Hoá'
    elif re.search('..CA.', df['CLASS']) and df['GENDER'] == 'F':
        return 'Nữ Chuyên Anh'
    elif re.search('..CA.', df['CLASS']) and df['GENDER'] == 'M':
        return 'Nam Chuyên Anh'
    elif re.search('..CTIN', df['CLASS']) and df['GENDER'] == 'F':
        return 'Nữ Chuyên Tin'
    elif re.search('..CTIN', df['CLASS']) and df['GENDER'] == 'M':
        return 'Nam Chuyên Tin'
    elif re.search('..CTRN', df['CLASS']) and df['GENDER'] == 'F':
        return 'Nữ CTRN'
    elif re.search('..CTRN', df['CLASS']) and df['GENDER'] == 'M':
        return 'Nam CTRN'
    elif re.search('..CSD', df['CLASS']) and df['GENDER'] == 'F':
        return 'Nữ CSĐ'
    elif re.search('..CSD', df['CLASS']) and df['GENDER'] == 'M':
        return 'Nam CSĐ'
    elif re.search('..TH.', df['CLASS']) or re.search('..SN', df['CLASS']) and df['GENDER'] == 'F':
        return 'Nữ TS'
    elif re.search('..TH.', df['CLASS']) or re.search('..SN', df['CLASS']) and df['GENDER'] == 'M':
        return 'Nam TS'
    elif re.search('..A.', df['CLASS']) and df['GENDER'] == 'F':
        return 'Nữ A'
    else:
        return 'Nam A'
    df['CLASS & GENDER'] = df.apply(cgag, axis=1)

def diem():
    def s1():
        st.plotly_chart(px.box(df, x = 'GENDER', y = 'S1'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'PYTHON-CLASS', y = 'S1'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'CLASS_GROUP', y = 'S1'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'KHỐI', y = 'S1'))
        st.write('Kết luận: ')
        def dtbs1():
            a = 0
            A = 0
            b = 0
            B = 0
            c = 0
            C = 0
            d = 0
            D = 0
            e = 0
            E = 0
            f = 0
            F = 0
            g = 0
            G = 0
            h = 0
            H = 0
            i = 0
            I = 0
            a = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S1']))
            A = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S1']))
            b = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S1']))
            B = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S1']))
            c = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S1']))
            C = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S1']))
            d = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S1']))
            D = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S1']))
            e = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S1']))
            E = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S1']))
            f = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S1']))
            F = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S1']))
            g = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S1']))
            G = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S1']))
            h = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S1']))
            H = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S1']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S1']))
            i = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S1']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S1']))
            I = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S1']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S1']))
            dtbs1 = {'Nữ Chuyên Toán': a, 'Nam Chuyên Toán': A, 'Nữ Chuyên Lý': b, 'Nam Chuyên Lý': B, 'Nữ Chuyên Hóa': c, 'Nam Chuyên Hóa': C, 
                    'Nữ Chuyên Văn': d, 'Nam Chuyên Văn': D, 'Nữ Chuyên Anh': e, 'Nam Chuyên Anh': E, 'Nữ Chuyên Tin': f, 'Nam Chuyên Tin': F, 
                    'Nữ CTRN': g, 'Nam CTRN': G, 'Nữ CSĐ': h, 'Nam CSĐ': H, 'Nữ A': i, 'Nam A': I}
            df['ĐTB S1'] = df['CLASS & GENDER'].map(dtbs1)
            return st.plotly_chart(px.histogram(df, x = 'CLASS_GROUP', color = 'GENDER', barmode = 'group', y = 'ĐTB S1'))
        dtbs1()
        st.write('Kết luận: ')
    def s2():
        st.plotly_chart(px.box(df, x = 'GENDER', y = 'S2'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'PYTHON-CLASS', y = 'S2'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'CLASS_GROUP', y = 'S2'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'KHỐI', y = 'S2'))
        st.write('Kết luận: ')
        def dtbs2():
            a = 0
            A = 0
            b = 0
            B = 0
            c = 0
            C = 0
            d = 0
            D = 0
            e = 0
            E = 0
            f = 0
            F = 0
            g = 0
            G = 0
            h = 0
            H = 0
            i = 0
            I = 0
            a = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S2']))
            A = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S2']))
            b = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S2']))
            B = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S2']))
            c = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S2']))
            C = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S2']))
            d = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S2']))
            D = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S2']))
            e = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S2']))
            E = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S2']))
            f = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S2']))
            F = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S2']))
            g = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S2']))
            G = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S2']))
            h = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S2']))
            H = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S2']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S2']))
            i = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S2']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S2']))
            I = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S2']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S2']))
            dtbs2 = {'Nữ Chuyên Toán': a, 'Nam Chuyên Toán': A, 'Nữ Chuyên Lý': b, 'Nam Chuyên Lý': B, 'Nữ Chuyên Hóa': c, 'Nam Chuyên Hóa': C,
                    'Nữ Chuyên Văn': d, 'Nam Chuyên Văn': D, 'Nữ Chuyên Anh': e, 'Nam Chuyên Anh': E, 'Nữ Chuyên Tin': f, 'Nam Chuyên Tin': F,
                    'Nữ CTRN': g, 'Nam CTRN': G, 'Nữ CSĐ': h, 'Nam CSĐ': H, 'Nữ A': i, 'Nam A': I}
            df['ĐTB S2'] = df['CLASS & GENDER'].map(dtbs2)
            return st.plotly_chart(px.histogram(df, x = 'CLASS_GROUP', color = 'GENDER', barmode = 'group', y = 'ĐTB S2'))
        dtbs2()
        st.write('Kết luận: ')
    def s3():
        st.plotly_chart(px.box(df, x = 'GENDER', y = 'S3'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'PYTHON-CLASS', y = 'S3'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'CLASS_GROUP', y = 'S3'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'KHỐI', y = 'S3'))
        st.write('Kết luận: ')
        def dtbs3():
            a = 0
            A = 0
            b = 0
            B = 0
            c = 0
            C = 0
            d = 0
            D = 0
            e = 0
            E = 0
            f = 0
            F = 0
            g = 0
            G = 0
            h = 0
            H = 0
            i = 0
            I = 0
            a = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S3']))
            A = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S3']))
            b = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S3']))
            B = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S3']))
            c = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S3']))
            C = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S3']))
            d = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S3']))
            D = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S3']))
            e = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S3']))
            E = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S3']))
            f = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S3']))
            F = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S3']))
            g = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S3']))
            G = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S3']))
            h = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S3']))
            H = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S3']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S3']))
            i = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S3']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S3']))
            I = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S3']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S3']))
            dtbs3 = {'Nữ Chuyên Toán': a, 'Nam Chuyên Toán': A, 'Nữ Chuyên Lý': b, 'Nam Chuyên Lý': B, 'Nữ Chuyên Hóa': c, 'Nam Chuyên Hóa': C,
                    'Nữ Chuyên Văn': d, 'Nam Chuyên Văn': D, 'Nữ Chuyên Anh': e, 'Nam Chuyên Anh': E, 'Nữ Chuyên Tin': f, 'Nam Chuyên Tin': F,
                    'Nữ CTRN': g, 'Nam CTRN': G, 'Nữ CSĐ': h, 'Nam CSĐ': H, 'Nữ A': i, 'Nam A': I}
            df['ĐTB S3'] = df['CLASS & GENDER'].map(dtbs3)
            return st.plotly_chart(px.histogram(df, x = 'CLASS_GROUP', color = 'GENDER', barmode = 'group', y = 'ĐTB S3'))
        dtbs3()
        st.write('Kết luận: ')
    def s4():
        st.plotly_chart(px.box(df, x = 'GENDER', y = 'S4'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'PYTHON-CLASS', y = 'S4'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'CLASS_GROUP', y = 'S4'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'KHỐI', y = 'S4'))
        st.write('Kết luận: ')
        def dtbs4():
            a = 0
            A = 0
            b = 0
            B = 0
            c = 0
            C = 0
            d = 0
            D = 0
            e = 0
            E = 0
            f = 0
            F = 0
            g = 0
            G = 0
            h = 0
            H = 0
            i = 0
            I = 0
            a = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S4']))
            A = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S4']))
            b = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S4']))
            B = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S4']))
            c = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S4']))
            C = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S4']))
            d = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S4']))
            D = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S4']))
            e = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S4']))
            E = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S4']))
            f = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S4']))
            F = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S4']))
            g = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S4']))
            G = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S4']))
            h = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S4']))
            H = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S4']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S4']))
            i = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S4']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S4']))
            I = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S4']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S4']))
            dtbs4 = {'Nữ Chuyên Toán': a, 'Nam Chuyên Toán': A, 'Nữ Chuyên Lý': b, 'Nam Chuyên Lý': B, 'Nữ Chuyên Hóa': c, 'Nam Chuyên Hóa': C,
                    'Nữ Chuyên Văn': d, 'Nam Chuyên Văn': D, 'Nữ Chuyên Anh': e, 'Nam Chuyên Anh': E, 'Nữ Chuyên Tin': f, 'Nam Chuyên Tin': F,
                    'Nữ CTRN': g, 'Nam CTRN': G, 'Nữ CSĐ': h, 'Nam CSĐ': H, 'Nữ A': i, 'Nam A': I}
            df['ĐTB S4'] = df['CLASS & GENDER'].map(dtbs4)
            return st.plotly_chart(px.histogram(df, x = 'CLASS_GROUP', color = 'GENDER', barmode = 'group', y = 'ĐTB S4'))
        dtbs4()
        st.write('Kết luận: ')
    def s5():
        st.plotly_chart(px.box(df, x = 'GENDER', y = 'S5'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'PYTHON-CLASS', y = 'S5'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'CLASS_GROUP', y = 'S5'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'KHỐI', y = 'S5'))
        st.write('Kết luận: ')
        def dtbs5():
            a = 0
            A = 0
            b = 0
            B = 0
            c = 0
            C = 0
            d = 0
            D = 0
            e = 0
            E = 0
            f = 0
            F = 0
            g = 0
            G = 0
            h = 0
            H = 0
            i = 0
            I = 0
            a = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S5']))
            A = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S5']))
            b = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S5']))
            B = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S5']))
            c = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S5']))
            C = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S5']))
            d = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S5']))
            D = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S5']))
            e = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S5']))
            E = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S5']))
            f = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S5']))
            F = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S5']))
            g = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S5']))
            G = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S5']))
            h = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S5']))
            H = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S5']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S5']))
            i = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S5']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S5']))
            I = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S5']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S5']))
            dtbs5 = {'Nữ Chuyên Toán': a, 'Nam Chuyên Toán': A, 'Nữ Chuyên Lý': b, 'Nam Chuyên Lý': B, 'Nữ Chuyên Hóa': c, 'Nam Chuyên Hóa': C,
                    'Nữ Chuyên Văn': d, 'Nam Chuyên Văn': D, 'Nữ Chuyên Anh': e, 'Nam Chuyên Anh': E, 'Nữ Chuyên Tin': f, 'Nam Chuyên Tin': F,
                    'Nữ CTRN': g, 'Nam CTRN': G, 'Nữ CSĐ': h, 'Nam CSĐ': H, 'Nữ A': i, 'Nam A': I}
            df['ĐTB S5'] = df['CLASS & GENDER'].map(dtbs5)
            return st.plotly_chart(px.histogram(df, x = 'CLASS_GROUP', color = 'GENDER', barmode = 'group', y = 'ĐTB S5'))
        dtbs5()
        st.write('Kết luận: ')
    def s6():
        st.plotly_chart(px.box(df, x = 'GENDER', y = 'S6'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'PYTHON-CLASS', y = 'S6'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'CLASS_GROUP', y = 'S6'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'KHỐI', y = 'S6'))
        st.write('Kết luận: ')
        def dtbs6():
            a = 0
            A = 0
            b = 0
            B = 0
            c = 0
            C = 0
            d = 0
            D = 0
            e = 0
            E = 0
            f = 0
            F = 0
            g = 0
            G = 0
            h = 0
            H = 0
            i = 0
            I = 0
            a = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S6']))
            A = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S6']))
            b = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S6']))
            B = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S6']))
            c = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S6']))
            C = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S6']))
            d = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S6']))
            D = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S6']))
            e = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S6']))
            E = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S6']))
            f = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S6']))
            F = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S6']))
            g = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S6']))
            G = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S6']))
            h = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S6']))
            H = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S6']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S6']))
            i = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S6']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S6']))
            I = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S6']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S6']))
            dtbs6 = {'Nữ Chuyên Toán': a, 'Nam Chuyên Toán': A, 'Nữ Chuyên Lý': b, 'Nam Chuyên Lý': B, 'Nữ Chuyên Hóa': c, 'Nam Chuyên Hóa': C,
                    'Nữ Chuyên Văn': d, 'Nam Chuyên Văn': D, 'Nữ Chuyên Anh': e, 'Nam Chuyên Anh': E, 'Nữ Chuyên Tin': f, 'Nam Chuyên Tin': F,
                    'Nữ CTRN': g, 'Nam CTRN': G, 'Nữ CSĐ': h, 'Nam CSĐ': H, 'Nữ A': i, 'Nam A': I}
            df['ĐTB S6'] = df['CLASS & GENDER'].map(dtbs6)
            return st.plotly_chart(px.histogram(df, x = 'CLASS_GROUP', color = 'GENDER', barmode = 'group', y = 'ĐTB S6'))
        dtbs6()
        st.write('Kết luận: ')
    def s7():
        st.plotly_chart(px.box(df, x = 'GENDER', y = 'S7'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'PYTHON-CLASS', y = 'S7'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'CLASS_GROUP', y = 'S7'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'KHỐI', y = 'S7'))
        st.write('Kết luận: ')
        def dtbs7():
            a = 0
            A = 0
            b = 0
            B = 0
            c = 0
            C = 0
            d = 0
            D = 0
            e = 0
            E = 0
            f = 0
            F = 0
            g = 0
            G = 0
            h = 0
            H = 0
            i = 0
            I = 0
            a = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S7']))
            A = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S7']))
            b = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S7']))
            B = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S7']))
            c = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S7']))
            C = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S7']))
            d = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S7']))
            D = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S7']))
            e = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S7']))
            E = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S7']))
            f = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S7']))
            F = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S7']))
            g = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S7']))
            G = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S7']))
            h = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S7']))
            H = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S7']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S7']))
            i = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S7']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S7']))
            I = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S7']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S7']))
            dtbs7 = {'Nữ Chuyên Toán': a, 'Nam Chuyên Toán': A, 'Nữ Chuyên Lý': b, 'Nam Chuyên Lý': B, 'Nữ Chuyên Hóa': c, 'Nam Chuyên Hóa': C,
                    'Nữ Chuyên Văn': d, 'Nam Chuyên Văn': D, 'Nữ Chuyên Anh': e, 'Nam Chuyên Anh': E, 'Nữ Chuyên Tin': f, 'Nam Chuyên Tin': F,
                    'Nữ CTRN': g, 'Nam CTRN': G, 'Nữ CSĐ': h, 'Nam CSĐ': H, 'Nữ A': i, 'Nam A': I}
            df['ĐTB S7'] = df['CLASS & GENDER'].map(dtbs7)
            return st.plotly_chart(px.histogram(df, x = 'CLASS_GROUP', color = 'GENDER', barmode = 'group', y = 'ĐTB S7'))
        dtbs7()
        st.write('Kết luận: ')
    def s8():
        st.plotly_chart(px.box(df, x = 'GENDER', y = 'S8'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'PYTHON-CLASS', y = 'S8'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'CLASS_GROUP', y = 'S8'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'KHỐI', y = 'S8'))
        st.write('Kết luận: ')
        def dtbs8():
            a = 0
            A = 0
            b = 0
            B = 0
            c = 0
            C = 0
            d = 0
            D = 0
            e = 0
            E = 0
            f = 0
            F = 0
            g = 0
            G = 0
            h = 0
            H = 0
            i = 0
            I = 0
            a = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S8']))
            A = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S8']))
            b = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S8']))
            B = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S8']))
            c = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S8']))
            C = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S8']))
            d = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S8']))
            D = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S8']))
            e = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S8']))
            E = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S8']))
            f = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S8']))
            F = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S8']))
            g = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S8']))
            G = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S8']))
            h = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S8']))
            H = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S8']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S8']))
            i = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S8']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S8']))
            I = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S8']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S8']))
            dtbs8 = {'Nữ Chuyên Toán': a, 'Nam Chuyên Toán': A, 'Nữ Chuyên Lý': b, 'Nam Chuyên Lý': B, 'Nữ Chuyên Hóa': c, 'Nam Chuyên Hóa': C,
                    'Nữ Chuyên Văn': d, 'Nam Chuyên Văn': D, 'Nữ Chuyên Anh': e, 'Nam Chuyên Anh': E, 'Nữ Chuyên Tin': f, 'Nam Chuyên Tin': F,
                    'Nữ CTRN': g, 'Nam CTRN': G, 'Nữ CSĐ': h, 'Nam CSĐ': H, 'Nữ A': i, 'Nam A': I}
            df['ĐTB S8'] = df['CLASS & GENDER'].map(dtbs8)
            return st.plotly_chart(px.histogram(df, x = 'CLASS_GROUP', color = 'GENDER', barmode = 'group', y = 'ĐTB S8'))
        dtbs8()
        st.write('Kết luận: ')
    def s9():
        st.plotly_chart(px.box(df, x = 'GENDER', y = 'S9'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'PYTHON-CLASS', y = 'S9'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'CLASS_GROUP', y = 'S9'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'KHỐI', y = 'S9'))
        st.write('Kết luận: ')
        def dtbs9():
            a = 0
            A = 0
            b = 0
            B = 0
            c = 0
            C = 0
            d = 0
            D = 0
            e = 0
            E = 0
            f = 0
            F = 0
            g = 0
            G = 0
            h = 0
            H = 0
            i = 0
            I = 0
            a = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S9']))
            A = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S9']))
            b = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S9']))
            B = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S9']))
            c = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S9']))
            C = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S9']))
            d = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S9']))
            D = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S9']))
            e = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S9']))
            E = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S9']))
            f = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S9']))
            F = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S9']))
            g = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S9']))
            G = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S9']))
            h = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S9']))
            H = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S9']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S9']))
            i = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S9']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S9']))
            I = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S9']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S9']))
            dtbs9 = {'Nữ Chuyên Toán': a, 'Nam Chuyên Toán': A, 'Nữ Chuyên Lý': b, 'Nam Chuyên Lý': B, 'Nữ Chuyên Hóa': c, 'Nam Chuyên Hóa': C,
                    'Nữ Chuyên Văn': d, 'Nam Chuyên Văn': D, 'Nữ Chuyên Anh': e, 'Nam Chuyên Anh': E, 'Nữ Chuyên Tin': f, 'Nam Chuyên Tin': F,
                    'Nữ CTRN': g, 'Nam CTRN': G, 'Nữ CSĐ': h, 'Nam CSĐ': H, 'Nữ A': i, 'Nam A': I}
            df['ĐTB S9'] = df['CLASS & GENDER'].map(dtbs9)
            return st.plotly_chart(px.histogram(df, x = 'CLASS_GROUP', color = 'GENDER', barmode = 'group', y = 'ĐTB S9'))
        dtbs9()
        st.write('Kết luận: ')
    def s10():
        st.plotly_chart(px.box(df, x = 'GENDER', y = 'S10'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'PYTHON-CLASS', y = 'S10'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'CLASS_GROUP', y = 'S10'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'KHỐI', y = 'S10'))
        st.write('Kết luận: ')
        def dtbs10():
            a = 0
            A = 0
            b = 0
            B = 0
            c = 0
            C = 0
            d = 0
            D = 0
            e = 0
            E = 0
            f = 0
            F = 0
            g = 0
            G = 0
            h = 0
            H = 0
            i = 0
            I = 0
            a = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['S10']))
            A = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['S10']))
            b = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['S10']))
            B = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['S10']))
            c = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['S10']))
            C = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['S10']))
            d = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['S10']))
            D = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['S10']))
            e = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['S10']))
            E = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['S10']))
            f = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['S10']))
            F = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['S10']))
            g = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['S10']))
            G = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['S10']))
            h = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['S10']))
            H = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S10']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['S10']))
            i = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S10']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['S10']))
            I = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S10']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['S10']))
            dtbs10 = {'Nữ Chuyên Toán': a, 'Nam Chuyên Toán': A, 'Nữ Chuyên Lý': b, 'Nam Chuyên Lý': B, 'Nữ Chuyên Hóa': c, 'Nam Chuyên Hóa': C,
                    'Nữ Chuyên Văn': d, 'Nam Chuyên Văn': D, 'Nữ Chuyên Anh': e, 'Nam Chuyên Anh': E, 'Nữ Chuyên Tin': f, 'Nam Chuyên Tin': F,
                    'Nữ CTRN': g, 'Nam CTRN': G, 'Nữ CSĐ': h, 'Nam CSĐ': H, 'Nữ A': i, 'Nam A': I}
            df['ĐTB S10'] = df['CLASS & GENDER'].map(dtbs10)
            return st.plotly_chart(px.histogram(df, x = 'CLASS_GROUP', color = 'GENDER', barmode = 'group', y = 'ĐTB S10'))
        dtbs10()
        st.write('Kết luận: ')
    def gpa():
        st.plotly_chart(px.box(df, x = 'GENDER', y = 'GPA'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'PYTHON-CLASS', y = 'GPA'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'CLASS_GROUP', y = 'GPA'))
        st.write('Kết luận: ')
        st.plotly_chart(px.box(df, x = 'KHỐI', y = 'GPA'))
        st.write('Kết luận: ')
        def dtbgpa():
            a = 0
            A = 0
            b = 0
            B = 0
            c = 0
            C = 0
            d = 0
            D = 0
            e = 0
            E = 0
            f = 0
            F = 0
            g = 0
            G = 0
            h = 0
            H = 0
            i = 0
            I = 0
            a = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'F')]['GPA']))
            A = sum(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Toán') & (df['GENDER'] == 'M')]['GPA']))
            b = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'F')]['GPA']))
            B = sum(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Lý') & (df['GENDER'] == 'M')]['GPA']))
            c = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'F')]['GPA']))
            C = sum(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Hóa') & (df['GENDER'] == 'M')]['GPA']))
            d = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'F')]['GPA']))
            D = sum(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Văn') & (df['GENDER'] == 'M')]['GPA']))
            e = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'F')]['GPA']))
            E = sum(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Anh') & (df['GENDER'] == 'M')]['GPA']))
            f = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'F')]['GPA']))
            F = sum(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Tin') & (df['GENDER'] == 'M')]['GPA']))
            g = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'F')]['GPA']))
            G = sum(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Trung Nhật') & (df['GENDER'] == 'M')]['GPA']))
            h = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'F')]['GPA']))
            H = sum(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Chuyên Sử Địa') & (df['GENDER'] == 'M')]['GPA']))
            i = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'F')]['GPA']))
            I = sum(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['GPA']/len(df[(df['CLASS_GROUP'] == 'Tích Hợp/Song Ngữ') & (df['GENDER'] == 'M')]['GPA']))
            dtbgpa = {'Nữ Chuyên Toán': a, 'Nam Chuyên Toán': A, 'Nữ Chuyên Lý': b, 'Nam Chuyên Lý': B, 'Nữ Chuyên Hóa': c, 'Nam Chuyên Hóa': C,
                    'Nữ Chuyên Văn': d, 'Nam Chuyên Văn': D, 'Nữ Chuyên Anh': e, 'Nam Chuyên Anh': E, 'Nữ Chuyên Tin': f, 'Nam Chuyên Tin': F,
                    'Nữ CTRN': g, 'Nam CTRN': G, 'Nữ CSĐ': h, 'Nam CSĐ': H, 'Nữ A': i, 'Nam A': I}
            df['ĐTB GPA'] = df['CLASS & GENDER'].map(dtbgpa)
            return st.plotly_chart(px.histogram(df, x = 'CLASS_GROUP', color = 'GENDER', barmode = 'group', y = 'ĐTB GPA'))
        dtbgpa()
        st.write('Kết luận: ')

p = st.radio('Điểm từng session', ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'GPA'))
if p == 'S1':
    st.write(s1)
elif p == 'S2':
    st.write(s2)
elif p == 'S3': 
    st.write(s3)
elif p == 'S4':
    st.write(s4)
elif p == 'S5':
    st.write(s5)
elif p == 'S6':
    st.write(s6)
elif p == 'S7':
    st.write(s7)
elif p == 'S8':
    st.write(s8)
elif p == 'S9':
    st.write(s9)
elif p == 'S10':
    st.write(s10)
elif p == 'GPA':
    st.write(gpa)