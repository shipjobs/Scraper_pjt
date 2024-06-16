프로젝트 명: 전국 빈집 시골집 데이터 수집 웹 스크래퍼

목적

- Web 상의 국내 시골집/빈집 매물 대행 사이트에서의 데이터 크롤링
- Web 상의 국내외 재건축 인테리어 이미지 데이터 크롤링 (학습, 디자인 생성 목적)

---

수집 정보

- 거래 매물 정보
- 건축/인테리어 정보

수집 대상

- 유튜브
- 페이스북
- 웹사이트

수집데이터

- **동영상/이미지 (url)**
- **텍스트 (매물 소개 문장) : **clob\*\*\*\*
- **댓글:clob**

저장소

- miniO
- PostgreSQL

---

주요기술

- Beautifulsoup
  - pip install Beautifulsoup
- playerwright
  - pip install playerwright
  - playerwright install

* flask
  - pip install flask

---

- ref
  - 강의 : 노마드코더
    - title: Python 으로 웹 스크래퍼 만들기
    - url: https://nomadcoders.co/python-for-beginners/lobby
  - 팀 필수 사항
    - requirements : 가상환경 requirements 활용 (참조: https://sosoeasy.tistory.com/597 )
