# Web_Crawler

우리가 프로젝트를 진행하며 데이터셋을 모아야 할 때에, 이를 하나씩 직접 다운받기엔 힘들 수 있습니다. <br/>
Web Crawler는 

## GET, POST











## header
우리는 컴퓨터에서 서버에 접속할 때, 요청 헤더를 전송합니다. (브라우저 정보 제공)
특정 사이트에선 Python-requests으로 접속을 하면 정보 제공을 하지 않습니다.
따라서 Chrome, Safari와 같은 브라우저로 접속한 것 처럼 해주기 위해 headers라는 매개변수를 변경해줄겁니다.

지금 접속중인 브라우저의 헤더 정보를 headers라는 매개변수에 넣어줄 수도 있습니다.

http://www.useragentstring.com/

위의 정보를 바탕으로 헤더 값을 수정하여
GET 메소드 호출할 때 함께 전달

```{.python}
header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15'}

url = 'github.com/hwk06023'

r = requests.get(url, headers = header)
```