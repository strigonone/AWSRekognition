import Test_Rekognition as tester
import jsonreader as jr

def main():
    output = jr.json_parser()
    for out in output:
        tester.TestImages(str(out), "dog".upper()).test_labelname()

if __name__ == "__main__":
    main()