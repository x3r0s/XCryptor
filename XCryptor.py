import os
import sys
import getpass
import argparse
import cryptoModule

bufferSize = 64 * 1024

swver = "1.0.1"

parser = argparse.ArgumentParser("--help", "-h", description="명령어 목록을 출력합니다.")

# 입력받을 인자값 등록
parser.add_argument("--input", "-i", required=True, help="대상 파일")
parser.add_argument("--output", "-o", required=False, help="암/복호화 되어 새로 생성될 파일")
parser.add_argument("--encrypt", "-e", required=False, action="store_true", default=True, help="암호화 모드")
parser.add_argument("--decrypt", "-d", required=False, action="store_true", default=False, help="복호화 모드")
parser.add_argument("--remove", "-r", required=False, action="store_true", default=False, help="암/복호화 후 대상 파일을 삭제")

# 입력받은 인자값을 args에 저장 (type: namespace)
args = parser.parse_args()

# Main Function
def main():
    # 대상 파일이 존재하지 않을 경우
    # 에러 내용 고지 후 프로그램 종료
    if not os.path.isfile(args.input):
        print("\033[31m존재하지 않는 파일입니다.\033[0m")
        return

    # 복호화 모드일 경우
    if args.decrypt:
        if args.input == args.output:
            print("\033[31m복호화 대상 파일과 새로 생성될 파일의 이름이 같을 수 없습니다.\033[0m")
            return

        if args.output == None:
            output = args.input.replace(".enc", '')
        else:
            output = args.output

        if os.path.exists(output):
            print("\033[31m새로 생성될 파일과 같은 이름을 가진 파일이 이미 존재합니다.\033[0m")
            return
        if args.output == None and os.path.exists(args.input.replace(".enc", '')):
            print("\033[31m새로 생성될 파일과 같은 이름을 가진 파일이 이미 존재합니다.\033[0m")
            return

        while True:
            # 유저에게 암호 키를 입력받음
            print("복호화 키를 입력해주세요")
            password = getpass.getpass()
            # 입력 받은 암호 키를 사용하여 복호화 진행
            try:
                cryptoModule.decryptFile(args.input, output, password, bufferSize)
                print(f"복호화 성공 => {os.path.basename(output)}")
                break
            # 암호가 일치하지 않을 경우
            except ValueError:
                print("암호가 옳바르지 않습니다. 암호를 다시 입력해주세요")
                continue
        
        # 만약 remove 옵션이 활성화 상태라면, 대상 파일 삭제
        if args.remove == True:
            os.remove(args.input)

    # 암호화 모드일 경우
    else:
        if args.input == args.output:
            print("\033[31m암호화 대상 파일과 새로 생성될 파일의 이름이 같을 수 없습니다.\033[0m")
            return
        if args.output == None:
            output = args.input + ".enc"
        else:
            output = args.output

        # 유저에게 암호 키를 입력받음
        print("암호화 키를 입력해주세요")
        password = getpass.getpass()

        # 입력받은 암호키로 암호화 진행
        cryptoModule.encryptFile(args.input, output, password, bufferSize)
        print(f"암호화 성공 => {os.path.basename(output)}")

        # 만약 remove 옵션이 활성화 상태라면, 대상 파일 삭제
        if args.remove == True:
            os.remove(args.input)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
