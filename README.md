# mingk42_args_history
- parquet 파일의 정보를 cli 기반으로 조회

### Usage
```bash
$ my-history -s ls
ls 사용 횟수는 1234회 입니다.

$ my-history -t 10 -d 2024-07-17
  cmd  cnt
pyenv 4256
   cd 3472
  git 3396
mkdir 1932
  pip 1592
  cat 1368
   vi 1356
 sudo 1320
  pdm 1220
   rm 1104
```


### DevEnv setting
```bash
$ git clone <URL>
$ git <proj_name>
$ pyenv virtualenv 3.11 clean
$ pyenv clean
$ rm -rf .venv
$ pdm venv create
$ source .venv/bin/activate
$ pdm install
$ [pdm test | pdm test]

# optional
$ pdm add -dG test pytest pytest-cov
```

### deploy
```bash
# dev branch
$ pip install git+https://github.com/Mingk42/mah_20240725.git@<branch name>

# main
$ pip install git+https://github.com/Mingk42/mah_20240725.git
```


### Ref
- [docs 바로가기](https://pdm-project.org/en/latest/usage/dependency/#add-development-only-dependencies)
