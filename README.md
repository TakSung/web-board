# Backend
It is a project to build a shopping mall backend using python.

# How to Start
## Downlode Code

```bash
git clone https://github.com/TakSung/web-board.git
cd web-board
pip install -r requirements.txt
```

# Requirements
```bash
# python<=3.11
pip install -r requirements.txt
```

# 과거 커밋부터 확인하기

### 원하는 커밋 히스토리 찾기
```bash
git log --oneline
```
- 그중에 원하는 커밋 히스토리의 해시값 복사

### 처음부터 하나씩 올라가며 공부하기
```bash
# 원하는 시점으로 이동
git checkout 76b00d2 # 76b00d2는 해시값으로 다른 값으로 대치가능

# 원하는 시점에 새로운 브랜치 생성. 원래 코드에 영향을 미치지 않음
git checkout -b study # study는 브랜치 이름으로 다른 이름으로 대치가능

# 다음 커밋으로 넘어가고 싶은 경우
git rebase f257f84 # f257f84는 해시값으로 다른 값으로 대치가능
```
- 진행중 충돌이 일어난 경우 아래 두 방법중 하나로 해결할 하길 추천한다.
- 안되면, 검색과 chatgpt를 찾아보자
```bash
# 현제 stage에 있는 변경사항을 버린다.
git stash

# 머지 되기 이전 커밋으로 돌아간다 (hard는 완전히 제거하는 옵션이다. 보존하길 원한다면, 새로 브랜치를 만들자)
git reset --hard 8ea0e53 # 8ea0e53는 해시값으로 다른 값으로 대치가능
```
