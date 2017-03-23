텍스트 파일 일괄 치환 스크립트 (maptext.py)
====

## 사전 정의

이 스크립트를 사용하기 위해서는 먼저 텍스트 치환을 위한 사전을 준비해야 한다.

사전은 [CSV 형식](https://ko.wikipedia.org/wiki/CSV_(%ED%8C%8C%EC%9D%BC_%ED%98%95%EC%8B%9D))의 파일로 작성해야 한다.

사전 파일은 두 개의 열으로 구성되어야 하며, 첫번째 열은 매치되어야 할 텍스트, 두번째 열은 치환되어야 할 텍스트다. 또한 헤더 역할을 하는 첫 번째 행의 내용은 반드시 `src,dst` 여야 한다.

예)

```
src,dst
"파이선","파이썬"
"programing","programming"
"acheive","acheive"
"accross","across"
"comming","coming"
"freind","friend"
"lollypop","lollipop"
"politican","politician"
"sence","sense"
"suprise","surprise"
"threshhold","threshold"
"whereever","wherever"
```


## 사용법

이 스크립트를 다운로드한 후 쉘에 다음과 같은 명령을 입력한다.

```
python maptext.py -d 사전파일 -o 출력파일 원본파일1 원본파일2 ...
```

원본 파일을 여러 개 지정한 경우 지정한 순서대로 모두 합친 후 치환한다.


### 옵션

* `-h`: 도움말 출력
* `-d`: 사전 파일 (기본값: `dic.csv`)
* `-o`: 출력 파일 (기본값: `replaced_text.{timestamp}.txt`)


### 예

```
python maptext.py -d 사전.csv -o 결과.md 원고1.md 원고2.md
```


