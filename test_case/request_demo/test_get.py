import allure
import requests


@allure.feature('get请求')
@allure.story('无参数')
@allure.title('用例名1')
def test_no_params():
    r = requests.get("http://www.baidu.com/")
    print(r.text)


# def test_no_params1():
#     r = requests.request(method='get',url="http://www.baidu.com/")
#     print(r.text)
#
#
# def test_no_params2():
#     sess = requests.session()
#     r = sess.request(method='get',url="http://www.baidu.com/")
#     print(r.text)

@allure.feature('get请求')
@allure.story('带参数')
@allure.title('用例名2')
def test_get_query():
    # get 请求带参数
    params = {'accountName':'ysy0226'}
    r = requests.request('get','http://qa.yansl.com:8084/acc/getAccInfo',params=params)#请求是以params关键字传参
    print(r.text)

@allure.feature('get请求')
@allure.story('带path参数')
@allure.title('用例名3')
def test_get_path():
    # get 请求参数在path中
    # 使用.format进行字符串格式化
    r = requests.request('get','http://qa.yansl.com:8084/acc/getAllAccs/{}/{}'.format(1,10))
    print(r.text)

@allure.feature('get请求')
@allure.story('下载文件')
@allure.title('用例名4')
def test_get_file(pub_data):
    # get 请求下载文件
    with allure.step('first,准备测试数据'):pass
    p = {'pridCode':'tyq287'}
    h = {'token':pub_data['token']}
    with allure.step('second,发送请求'):pass
    r = requests.request('get','http://qa.yansl.com:8084/product/downProdRepertory',params=p,headers=h)
    # r.content获取响应正文的字节码
    with allure.step('third,请求数据'):
        allure.attach('请求行，请求头，请求正文','请求信息',allure.attachment_type.TEXT)
    with open('ysy.xls','wb') as f:
        f.write(r.content)



