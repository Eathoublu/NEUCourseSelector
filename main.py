import requests
import urllib
import urllib3
import http.cookiejar
import re
# import threading

studentNo = input('>>>请输入您的学号：')
studentPa = input('>>>请输入您的密码：')

data = urllib.parse.urlencode({
  'strStudentNO': studentNo,
  'strPassword': studentPa,
  'imageOK.x': '21',
  'imageOK.y': '15'
}).encode('utf-8')

headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}
CourseNO = input('>>>请键入课程编号（在您班学委提供的课程名单里面可以找到）：')
cookieJar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJar))
req1 = urllib.request.Request('http://aao.courseselection.aiursoft.com/LOGIN_LOGININ.XKAPPPROCESS',headers=headers,data=data)
rs1 = opener.open(req1)
# print(rs1.read().decode('gbk'))
# print(cookieJar)
# 登陆成功

req2 = urllib.request.Request('http://aao.courseselection.aiursoft.com/XK_DISPXKRESULT.XKAPPPROCESS?',headers=headers)
rs2 = opener.open(req2)
# print(rs2.read().decode('gbk'))
# 获取课程表成功

req3 = urllib.request.Request('http://aao.courseselection.aiursoft.com/XK_GETTASKINFOBYCOURSE.XKAPPPROCESS?'+'CourseNO='+CourseNO+'&MajorLevel=05&'+'&MajorLevel=05&GradeYear=2017&MajorNO=14&CourseModelID=3&IfNeed=-1',headers=headers)
rs3 = opener.open(req3)
text = str(rs3.read().decode('gbk'))
# print(text)
XKTaskID = re.findall('onClick="(.*?)"',text)[0][7:-6]
print(XKTaskID)
# CurTaskID=484878;
# 访问老师课程信息成功
for i in range(10):
  req4 = urllib.request.Request('http://aao.courseselection.aiursoft.com/XK_SELECTCOURSE.XKAPPPROCESS?XKTaskID='+XKTaskID,headers=headers)
  rs4 = opener.open(req4)
  text2 = rs4.read().decode('gbk')
  print(text2)
  if '选课成功' in text2:
    print('恭喜你！选成功啦！')
    break

# if '选课人数达到上限'or'该课程性质门数超出限制' in text2:
#     print('这个课程选不了了噢')
