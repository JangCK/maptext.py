import argparse
import csv
import datetime

description = """텍스트 파일의 내용을 DICFILE의 규칙에 따라 치환하여 OUTFILE로 저장한다."""


def parse_args():
    """명령행 인자를 해석한다."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
            dest='filenames',
            metavar='filename',
            nargs='*',
    )
    parser.add_argument(
            '-d',
            dest='dicfile',
            action='store',
            default='dic.csv',
            help='사전 파일(CSV)',
    )
    parser.add_argument(
            '-o',
            dest='outfile',
            action='store',
            default='replaced_text.' + str(datetime.datetime.now().timestamp()) + '.txt',
            help='출력 파일',
    )

    args = parser.parse_args()

    if not args.filenames:
        print('오류: 원본 파일이 지정되지 않았습니다.\n\n')
        parser.print_help()
        return None

    return args


def load_csv(filename):
    """CSV 파일을 읽어 dict를 생성한다."""
    try:
        with open(filename, 'r', encoding='utf-8-sig', newline='') as file:
            rows = list(csv.DictReader(file))
    except FileNotFoundError:
        print('CSV 파일을 찾을 수 없습니다: ' + filename)
        return None
    except UnicodeDecodeError:
        print('CSV 파일의 인코딩을 UTF-8로 바꾸어 주세요: ' + filename)
        return None
    return rows


def load_text(filenames):
    """텍스트 파일들을 읽어 하나로 모은다."""
    text = ''
    for filename in filenames:
        try:
            with open(filename, 'r', encoding='utf-8-sig', newline='') as file:
                text += file.read()
        except FileNotFoundError:
            print('원본 파일을 찾을 수 없습니다: ' + filename)
            return None
        except UnicodeDecodeError:
            print('원본 파일의 인코딩을 UTF-8로 바꾸어 주세요: ' + filename)
            return None
    return text


def map_text(dic, text):
    """text를 dic에 의해 치환한다."""
    for item in dic:
        src = item['src']
        dst = item['dst']
        count = text.count(src)
        text = text.replace(src, dst)
        print(count, '개 치환:', src, '=>', dst)
    return text


def write_text(outfile, text):
    """text를 파일로 저장한다."""
    with open(outfile, 'w', encoding='utf-8') as file:
        file.write(text)


def main():
    # 명령행 인자 해석
    args = parse_args()
    if args is None:
        exit(1)
    
    # 사전 파일 로드
    dic = load_csv(args.dicfile)
    if dic is None:
        exit(1)

    # 원본 텍스트 파일 로드
    text = load_text(args.filenames)
    if text is None:
        exit(1)

    # 치환
    replaced_text = map_text(dic, text)

    # 저장
    write_text(args.outfile, replaced_text)


if __name__ == '__main__': 
    main()

