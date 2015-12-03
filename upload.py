#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import codecs
import instagram


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('image', help='Square preconverted image')
    parser.add_argument('--login', help='Instagram login', required=True)
    parser.add_argument('--password', help='Instagram password', required=True)

    parser.add_argument('--comment', '-c', help='Short comment can be posted right from here')
    parser.add_argument('--long-comment', '-C', help='File with utf-8 long comment')
    return parser.parse_args()


def main(args):
    insta = instagram.InstagramSession()
    if insta.login(args.login, args.password):
        print 'Logged in as %s' % args.login
        media_id = insta.upload_photo(args.image)
        print media_id
        if media_id is not None:
            text = u''
            if args.long_comment:
                for line in codecs.open(args.long_comment, encoding='utf-8'):
                    text += line
            elif args.comment:
                text = args.comment

            if len(text) > 0:
                insta.configure_photo(media_id, text)
    print 'Done'


if __name__ == "__main__":
    main(parse_args())
