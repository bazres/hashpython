import hashlib
import argparse
import os
def main(text, hashtype):
    encoder = text.encode('utf-8')
    myhash = ''

    if hashtype.lower() == 'md5':
        myhash = hashlib.md5(encoder).hexdigest()
    elif hashtype.lower() == 'sha1':
        myhash = hashlib.sha1(encoder).hexdigest()
    elif hashtype.lower() == 'sha224':
        myhash = hashlib.sha1(encoder).hexdigest()
    elif hashtype.lower() == 'sha256':
        myhash = hashlib.sha1(encoder).hexdigest()
    elif hashtype.lower() == 'sha384':
        myhash = hashlib.sha1(encoder).hexdigest()
    elif hashtype.lower() == 'sha512':
        myhash = hashlib.sha1(encoder).hexdigest()
    else:
        print("[!]  The Script dose not support this hash type")
        exit(0)

    print("Your hash is : ", myhash)

    file = open("hash.txt", 'w')
    file.write(myhash)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='convert text to hash')
    parser.add_argument('-t', '--text', dest = 'text', required=True)
    parser.add_argument('-T', '--Type', dest='type', required=True)
    args = parser.parse_args()

    txt = args.text
    htype= args.type
    main(txt, htype)



