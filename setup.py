# hello jisun
# 과 같이 명령어를 입력하기 위한 설정 파일
# python setup.py install
# 설치 후 사용 가능
from setuptools import setup, find_packages


setup(
    # 모듈명
    name = 'hello',
    # 버전
    version = '1.0.0',
    author = 'Jisun',
    author_email = 'fpdldk912@gmail.com',
    description = 'Greet someone',
    packages = find_packages(),
    entry_points = {
        "console_scripts": [
            # hello라는 명령어를 실행하면
            # hello 모듈 main.py에서 main함수를 실행한다는 의미
            "hello = hello.main:main"
        ]
    },
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)