import requests



def test_post_json():
    data = {
  "pwd": "HF123456",
  "userName": "huang123"
}
    r=requests.post('http://qa.yansl.com:8084/login',json=data)
    print(r.text)




def test_post_json1(pub_data):
    data = {
  "pwd": "HF123456",
  "userName": "huang123"
}
    h = {'token':pub_data['token']}
    r = requests.post('http://qa.yansl.com:8084/login', json=data,headers=h)#json关键字发送json类型数据
    print(r.text)



def test_post_formdata(pub_data):
    data = {
  "userName": "lijc1010"
}
    h = {'token':pub_data['token']}
    r = requests.post('http://qa.yansl.com:8084/login', data=data,headers=h)#data关键字发送json类型数据
    print(r.text)



def test_post_upload_file(pub_data):
    # post请求上传文件
    data ={'file':open('ysy.xls','rb')}
    h = {'token':pub_data['token']}
    r = requests.post('http://qa.yansl.com:8084/product/uploaProdRepertory',files=data,headers=h)
    print(r.text)




