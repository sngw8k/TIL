# git

## 버전 관리란?
“버전 관리” 는 무엇이고 우리는 왜 이것을 알아야 할까? 버전 관리 시스템은 파일 변화를 시간에 따라 기록했다가 나중에 특정 시점의 버전을 다시 꺼내올 수 있는 시스템이다. 이 책에서는 버전 관리하는 예제로 소프트웨어 소스 코드만 보여주지만, 실제로 거의 모든 컴퓨터 파일의 버전을 관리할 수 있다.

## 분산 버전 관리 시스템 (DVCS)

DVCS에서의 클라이언트는 단순히 파일의 마지막 스냅샷을 Checkout 하지 않는다. 그냥 저장소를 히스토리와 더불어 전부 복제한다. 서버에 문제가 생기면 이 복제물로 다시 작업을 시작할 수 있다. 클라이언트 중에서 아무거나 골라도 서버를 복원할 수 있다. Clone은 모든 데이터를 가진 진정한 백업이다. 게다가 대부분의 DVCS 환경에서는 리모트 저장소가 존재한다. 리모트 저장소가 많을 수도 있다. 그래서 사람들은 동시에 다양한 그룹과 다양한 방법으로 협업할 수 있다. 계층 모델 같은 중앙집중식 시스템으로는 할 수 없는 워크플로를 다양하게 사용할 수 있다.

![DVCS](./assets/distributed.png)

## 세가지 상태

- Committed란 데이터가 로컬 데이터베이스에 안전하게 저장됐다는 것을 의미한다.
- Modified는 수정한 파일을 아직 로컬 데이터베이스에 커밋하지 않은 것을 말한다.
- Staged란 현재 수정한 파일을 곧 커밋할 것이라고 표시한 상태를 의미한다.

![areas](./assets/areas.png)

Git으로 하는 일은 기본적으로 아래와 같다.

1. 워킹 트리에서 파일을 수정한다.
2. Staging Area에 파일을 Stage 해서 커밋할 스냅샷을 만든다. 모든 파일을 추가할 수도 있고 선택하여 추가할 수도 있다.
3. Staging Area에 있는 파일들을 커밋해서 Git 디렉토리에 영구적인 스냅샷으로 저장한다.

## 명령어

```shell
git init
```
- `.git directory`를 생성하는 명렁어
- 현재 폴더에 `.git` 폴더를 생성

```shell
git add .
```
- `working directory`에 있는 파일, 폴더를 `staging area`에 추가
- add 하기전에 파일이 저장이 되었는지 확인하기
- `git add <file, folder name>` 으로 특정 폴더, 파일만 추가

```shell
git commit -m 'message'
```
- `staging area`에 올라간 파일들을 저장

```shell
git remote add origin <remote url>
```
- 원격 저장소 주소를 `origin`이라는 별명으로 저장

```shell
git push origin master
```
- `master` 브랜치를 `origin` 원격 저장소로 업로드

```shell
git pull origin master
```
- 원격 저장소에 마지막 코드 상태를 다운로드

```shell
git clone <remote url>
```
- 원격 저장소에 있는 레포를 현재 폴더에 복제
- 현재 폴더에서 open git bash를 통해 명령어 입력

```shell
git branch <branch name>
```
- `branch name` 이름을 가진 브랜치를 생성
- ` -d <branch name>` : `branch name` 브랜치를 삭제

```shell
git branch 
```
- 저장된 모든 branch 확인하는 명령어


```shell
git switch <branch name>
```
- 브랜치를 전환하는 명령어

## 설정

```shell
git status
```
- 현재 상태를 체크하는 명령어

```shell
git config
```
- git 설정을 하는 명령어
- 일반적으로 `--global` 옵션으로 최초 한번만 실행
- `git config --global user.email 'your@email.com'`
- `git config --global user.name 'yourname'`

```shell
git remote 
```
- remote 저장소 주소를 추가하는 명령어
- `git remote add origin <remoteurl>`
- `-v` (optional) : 연결되어있는 원격저장소 정보를 확인할 때


## 확장프로그램 (Extensions)
```
open in browser 
```
- 작업하고 있는 것을 브라우저에서 볼 수 있다.