# Web_Crawler

우리가 프로젝트를 진행하며 데이터 수집을 할 때에, 이를 하나씩 직접 다운받기엔 힘들 수 있습니다. <br/>
우리가 개발할 Web Crawler는 자동화 된 방법으로 데이터 수집을 도와줍니다. <br/>

## Requests
Requests는 Python에서 HTTP 요청을 보내는 HTTP 라이브러리입니다. <br/>
GET, POST, PUT, DELETE 등의 HTTP 메소드를 사용할 수 있으며 Data Encoding을 지원합니다.<br/>
requests는 직관적이며 빠른 속도로 데이터를 가져올 수 있다는 장점이 있습니다.<br/>
하지만 requests는 javascript에 둘러쌓인 데이터는 가져올 수 없다는 단점이 있습니다.<br/><br/>


### Install

**Windows**
```
pip install requests
```
**Mac**
```
pip3 install requests
```
<br/>


## Beautiful Soup
BeautifulSoup은 많은 사람들이 Web Crawler를 개발하기 위해 사용하는 라이브러리입니다. <br/>
Web Crawler를 통해 토큰화 되고 의미있는 형태의 데이터 수집을 위해 BeatifulSoup을 사용합니다. <br/>
BeautifulSoup은 위의 Requests 라이브러리를 통해 가져온 HTML 문자열 파일을  Python의 객체 구조로 변환해 주는 파싱 역할도 합니다. <br/>

> HTML에서 `<tag> </tag>`로 구성된 요소를 <u>Python 스럽게</u> 바꿔주는 느낌적인 느낌
<br/>

### Install

**Windows**
```
pip install bs4
```
**Mac**
```
pip3 install bs4
```
<br/>

## Selenium
위에서 javascript에 둘러싸여 있는 데이터는 가져올 수 없는 단점을 갖고 있다고 했었는데, 이를 보완해주기 위해 사용합니다. <br/>

그러나 javascript가 사용되지 않는 단순한 페이지의 크롤링이라면 방식 자체가 시간, 메모리 측면에서 비효율적이니 사용하지 않는 편이 더 좋습니다. <br/>
> HTML, CSS, 외부 js, 이미지 데이터 등 페이지의 모든 것을 가져오게 됨.

위와 같이 비효율적이라고 생각될 수 있지만, 브라우저를 제어하고, 브라우저가 하는 행동을 자동화 한다는 점에 있어서 매우 강력하기도 함. <br/>
> 그렇다고 Selenium이 브라우저까지 포함하고 있지는 않아서 WebDriver를 통해 컴퓨터에 내장되어 있는 브러우저를 사용함. <br/>

### Install

**Windows**
```
pip install selenium
```
**Mac**
```
pip3 install selenium
```
<br/>


## HTTP - GET, POST
HTTP(HyperText Transfer Protocol)는 WWW 상에서 정보를 주고 받을 수 있는 프로토콜입니다. <br/>

HTTP 요청 방식에는 GET 방식과 POST 방식이 존재합니다. <br/><br/>


### GET
**GET 방식은 데이터를 서버에서 가져오기만 하는 방식입니다.** <br/>
서버에서 데이터를 가져와서 보여주는 용도로 사용되지만, 서버의 값이나 상태에 변화를 주진 않습니다. <br/>

GET은 데이터가 header에 포함되어 전달됩니다. <br/>

GET은 URL에 변수를 포함해서 요청합니다. <br/>

> https://www.google.com/search?client=safari&rls=en&q=%EA%B9%80%ED%98%84%EC%9A%B0&ie=UTF-8&oe=UTF-8

위 URL 주소에서 GET 주소는 https://www.google.com/search 이며, <br/>
'?' 이후에 오는 'client=safari&rls=en&q=%EA%B9%80%ED%98%84%EC%9A%B0&ie=UTF-8&oe=UTF-8' 는 쿼리스트링이라 하는 파라미터 값입니다. <br/>



### POST
**POST 방식은 서버의 데이터에 변화를 주는 방식입나다.** <br/>
서버의 값이나 상태에 변화를 주며, GET 방식보다 많은 양의 데이터를 처리하기에도 적합합니다. <br/>

POST는 데이터가 body에서 key-value 형식으로 전달됩니다. <br/>
POST는 URL에 데이터가 노출되지 않습니다. <br/>



## header
우리는 컴퓨터에서 서버에 접속할 때, 요청 헤더를 전송합니다. (브라우저 정보 제공) <br/>
특정 사이트에선 Python-requests으로 접속을 하면 정보 제공을 하지 않습니다. <br/>
따라서 Chrome, Safari와 같은 브라우저로 접속한 것 처럼 해주기 위해 headers라는 매개변수를 변경해줄겁니다. <br/>

지금 접속중인 브라우저의 헤더 정보를 headers라는 매개변수에 넣어줄 수도 있습니다. <br/>

http://www.useragentstring.com/ <br/>

위의 정보를 바탕으로 헤더 값을 수정하여, GET 메소드 호출할 때 함께 전달합니다. <br/>

```{.python}
header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15'}

url = 'github.com/hwk06023'

r = requests.get(url, headers = header)
```