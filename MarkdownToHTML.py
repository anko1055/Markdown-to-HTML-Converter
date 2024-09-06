import markdown as md
import sys
import argparse

contents=""
def main(inputpath,outputpath):
    with open(inputpath,"r") as f:
        contents=f.read()
    html=md.markdown(contents,extensions=['tables'])
    with open(outputpath,"w")as f:
        f.write(html)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="MarkdownをHTMLに変換します。")
    parser.add_argument("input", help="入力Markdownファイルのパス")
    parser.add_argument("output", help="出力HTMLファイルのパス")

    args = parser.parse_args()
    main(args.input, args.output)


