import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# # 获取中证500成分股
# rs = bs.query_zz500_stocks()
# print('query_zz500 error_code:'+rs.error_code)
# print('query_zz500  error_msg:'+rs.error_msg)

# # 打印结果集
# zz500_stocks = []
# while (rs.error_code == '0') & rs.next():
#     # 获取一条记录，将记录合并在一起
#     zz500_stocks.append(rs.get_row_data())
# result = pd.DataFrame(zz500_stocks, columns=rs.fields)
# # 结果集输出到csv文件
# result.to_csv("/home/catmas/Documents/Python/STP/src/test/zz500_stocks.csv",
#               encoding="utf-8", index=False)
# print(result.to_string())

# 获取证券基本资料
rs = bs.query_stock_basic(code="")
# # rs = bs.query_stock_basic(code_name="浦发银行")  # 支持模糊查询
# print('query_stock_basic respond error_code:'+rs.error_code)
# print('query_stock_basic respond  error_msg:'+rs.error_msg)

# # 打印结果集
# data_list = []
# while (rs.error_code == '0') & rs.next():
#     # 获取一条记录，将记录合并在一起
#     data_list.append(rs.get_row_data())
# result = pd.DataFrame(data_list, columns=rs.fields)
# # 结果集输出到csv文件
# result.to_csv("/home/catmas/Documents/Python/STP/src/test/stock_basic.csv",
#               encoding="utf-8", index=False)
# print(result)

growth_list = []
while (rs.error_code == '0') & rs.next():
    rs_growth = bs.query_growth_data(code=rs[["code"]])
    while (rs_growth.error_code == '0') & rs_growth.next():
        growth_list.append(rs_growth.get_row_data())
        result_growth = pd.DataFrame(growth_list, columns=rs_growth.fields)
        result_growth.to_csv(
            "/home/catmas/Documents/Python/STP/src/test/growth_data.csv", encoding="utf-8", index=False)
    print(result_growth)

# 成长能力
# 打印输出
# 结果集输出到csv文件

# 登出系统
bs.logout()
