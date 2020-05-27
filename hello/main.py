# 파이썬으로 커맨드라인 프로그램 만들기
# python main.py jisun
# python main.py --help
import argparse
import sys


def hello(name):
    print("Hello, {}".format(name))


def bye(name):
    print('Good bye, {}'.format(name))


def main():
    parser = argparse.ArgumentParser()
    # argument 추가
    # nargs: argument의 개수, '?'이면 default값으로
    parser.add_argument('name', nargs='?', default=False, help="Put your name")
    
    # 버전 확인 옵션 추가
    # action: 해당 argument가 추가될 때 일어나는 액션
    # "store_true": version을 true로
    parser.add_argument('-v', '--version', action="store_true", help="Show version of this program")
    
    # 둘 중 하나만 사용할 수 있는 옵션
    # --hello 또는 --bye 둘 중 하나만을 사용할 수 있음
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--hello', action="store_true", help="say hello")
    group.add_argument('--bye', action="store_true", help="say good bye")
    
    args = parser.parse_args()

    name = args.name

    # 버전 정보
    if args.version:
        print('1.0.0')
        sys.exit()
    
    # argument를 입력하지 않았을 때
    if not name:
        parser.print_help() # 도움말 출력
        sys.exit()

    if args.hello:
        hello(name)
    else:
        bye(name)


if __name__=="__main__":
    main()