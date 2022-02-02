import argparse
from datetime import datetime
from pathlib import Path
import random
import re
import sys
'''
    Script for cooking MSR corpus
'''

RANDOM_SEED = {'as': 'AS', 'cityu': 'CITYU', 'msr': 'MSR', 'pku': 'PKU'}
VALID_RATIO = 0.1

# for data io

LINE_DELIM = '\n'  # Line
SL_TOKEN_DELIM = ' '
SL_ATTR_DELIM = '_'
SL_FORMAT = 'sl'
WL_FORMAT = 'wl'


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--quiet',
                        '-q',
                        action='store_true',
                        help='Do not report on screen')
    parser.add_argument('--dataset',
                        required=True,
                        choices=['as', 'cityu', 'msr', 'pku'])
    parser.add_argument('--train_data',
                        type=Path,
                        required=True,
                        help='File path to training data')
    parser.add_argument('--test_data',
                        type=Path,
                        required=True,
                        help='File path to test data')
    parser.add_argument('--output_data_path',
                        '-o',
                        type=Path,
                        default=None,
                        help='File path to output data')
    parser.add_argument('--input_data_format',
                        '-f',
                        default='utf8',
                        choices=['utf8', 'txt'])
    parser.add_argument('--output_data_format',
                        default='sl',
                        choices=['sl', 'wl'])
    parser.add_argument('--unshuffle',
                        action='store_true',
                        help='Specify to not shuffle data before cooking')

    args = parser.parse_args()
    return args


def normalize_input_line(line):
    line = re.sub(' +', ' ', line).strip(' \t\n')
    return line


def remove_whitespace_from_line(line):
    line = re.sub(' +', '', line).strip(' \t\n')
    return line


def load_data(path, data_format):
    if data_format == 'utf8':
        data = load_utf8_data(path)

    elif data_format == 'txt':
        data = load_txt_data(path)

    else:
        print('Error: invalid data format: {}'.format(data_format),
              file=sys.stderr)
        sys.exit()

    return data


def load_utf8_data(path):
    data = []
    with open(path, encoding='utf8') as f:
        for line in f:
            line = normalize_input_line(line)
            data.append(line)
    return data


def load_txt_data(path):
    raise NotImplementedError
    sys.exit()


def gen_div_data(data, data_format, dataset, shuffle=False, train=True):
    if data_format == SL_FORMAT:
        data = gen_div_data_SL(data, dataset, shuffle=shuffle, train=train)
    elif data_format == WL_FORMAT:
        data = gen_div_data_WL(data, dataset, shuffle=shuffle, train=train)
    return data


def gen_div_data_SL(data, dataset, shuffle=False, train=True):
    ls = data  # lines

    # shuffle
    if shuffle and train:
        random.Random(RANDOM_SEED[dataset]).shuffle(ls)

    # gen div data
    if train:
        train_div_data = ls[:int(len(ls) * (1.0 - VALID_RATIO))]
        valid_div_data = ls[int(len(ls) * (1.0 - VALID_RATIO)):]
        return train_div_data, valid_div_data
    else:
        test_div_data = ls
        return test_div_data


def gen_div_data_WL(data, dataset, shuffle=False, train=True):
    raise NotImplementedError
    sys.exit()


def log(message, file=sys.stderr):
    print(message, file=file)


def report(train_div_data, valid_div_data, test_div_data):
    train_sents = train_div_data
    valid_sents = valid_div_data
    test_sents = test_div_data

    # train
    train_n_sents = len(train_sents)

    train_ss = [s.split() for s in train_sents]
    train_ss_str = [''.join(s) for s in train_ss]
    train_ws = [w for s in train_ss for w in s]
    train_n_words = len(train_ws)

    train_cs = [c for w in train_ws for c in w]
    train_n_chars = len(train_cs)

    train_max_wps = len(max(train_ss, key=len))
    train_max_cps = len(max(train_ss_str, key=len))
    train_max_cpw = len(max(train_ws, key=len))

    train_min_wps = len(min(train_ss, key=len))
    train_min_cps = len(min(train_ss_str, key=len))
    train_min_cpw = len(min(train_ws, key=len))

    train_avg_wps = train_n_words / train_n_sents  # words/sentence
    train_avg_cps = train_n_chars / train_n_sents  # chars/sentence
    train_avg_cpw = train_n_chars / train_n_words  # chars/word

    # valid
    valid_n_sents = len(valid_sents)

    valid_ss = [s.split() for s in valid_sents]
    valid_ss_str = [''.join(s) for s in valid_ss]
    valid_ws = [w for s in valid_ss for w in s]
    valid_n_words = len(valid_ws)

    valid_cs = [c for w in valid_ws for c in w]
    valid_n_chars = len(valid_cs)

    valid_max_wps = len(max(valid_ss, key=len))
    valid_max_cps = len(max(valid_ss_str, key=len))
    valid_max_cpw = len(max(valid_ws, key=len))

    valid_min_wps = len(min(valid_ss, key=len))
    valid_min_cps = len(min(valid_ss_str, key=len))
    valid_min_cpw = len(min(valid_ws, key=len))

    valid_avg_wps = valid_n_words / valid_n_sents  # words/sentence
    valid_avg_cps = valid_n_chars / valid_n_sents  # chars/sentence
    valid_avg_cpw = valid_n_chars / valid_n_words  # chars/word

    # test
    test_n_sents = len(test_sents)

    test_ss = [s.split() for s in test_sents]
    test_ss_str = [''.join(s) for s in test_ss]
    test_ws = [w for s in test_ss for w in s]
    test_n_words = len(test_ws)

    test_cs = [c for w in test_ws for c in w]
    test_n_chars = len(test_cs)

    test_max_wps = len(max(test_ss, key=len))
    test_max_cps = len(max(test_ss_str, key=len))
    test_max_cpw = len(max(test_ws, key=len))

    test_min_wps = len(min(test_ss, key=len))
    test_min_cps = len(min(test_ss_str, key=len))
    test_min_cpw = len(min(test_ws, key=len))

    test_avg_wps = test_n_words / test_n_sents  # words/sentence
    test_avg_cps = test_n_chars / test_n_sents  # chars/sentence
    test_avg_cpw = test_n_chars / test_n_words  # chars/word

    log('### report')
    log('# [TRAIN] sent: {} ...'.format(len(train_sents)))
    log('# [TRAIN] word: {} ...'.format(train_n_words))
    log('# [TRAIN] char: {} ...'.format(train_n_chars))
    log('# [TRAIN] words/sent: min={} max={} avg={}'.format(
        train_min_wps, train_max_wps, train_avg_wps))
    log('# [TRAIN] chars/sent: min={} max={} avg={}'.format(
        train_min_cps, train_max_cps, train_avg_cps))
    log('# [TRAIN] chars/word: min={} max={} avg={}'.format(
        train_min_cpw, train_max_cpw, train_avg_cpw))
    log('####')
    log('# [VALID] sent: {} ...'.format(len(valid_sents)))
    log('# [VALID] word: {} ...'.format(valid_n_words))
    log('# [VALID] char: {} ...'.format(valid_n_chars))
    log('# [VALID] words/sent: min={} max={} avg={}'.format(
        valid_min_wps, valid_max_wps, valid_avg_wps))
    log('# [VALID] chars/sent: min={} max={} avg={}'.format(
        valid_min_cps, valid_max_cps, valid_avg_cps))
    log('# [VALID] chars/word: min={} max={} avg={}'.format(
        valid_min_cpw, valid_max_cpw, valid_avg_cpw))
    log('####')
    log('# [TEST] sent: {} ...'.format(len(test_sents)))
    log('# [TEST] word: {} ...'.format(test_n_words))
    log('# [TEST] char: {} ...'.format(test_n_chars))
    log('# [TEST] words/sent: min={} max={} avg={}'.format(
        test_min_wps, test_max_wps, test_avg_wps))
    log('# [TEST] chars/sent: min={} max={} avg={}'.format(
        test_min_cps, test_max_cps, test_avg_cps))
    log('# [TEST] chars/word: min={} max={} avg={}'.format(
        test_min_cpw, test_max_cpw, test_avg_cpw))


def cook(args):
    start_time = datetime.now().strftime('%Y%m%d_%H%M')
    if not args.quiet:
        log('Start time: {}\n'.format(start_time))
        log('### arguments')
        for k, v in args.__dict__.items():
            log('# {}={}'.format(k, v))
        log('')

    train_data_path = args.train_data
    test_data_path = args.test_data
    train_data = load_data(train_data_path, data_format=args.input_data_format)
    test_data = load_data(test_data_path, data_format=args.input_data_format)

    train_div_data, valid_div_data = gen_div_data(
        train_data,
        data_format=args.output_data_format,
        dataset=args.dataset,
        shuffle=not args.unshuffle,
        train=True)
    test_div_data = gen_div_data(test_data,
                                 data_format=args.output_data_format,
                                 dataset=args.dataset,
                                 shuffle=not args.unshuffle,
                                 train=False)

    if args.output_data_path:
        output_train_data_path = '{}/{}.train.seg.{}'.format(
            args.output_data_path, args.dataset, args.output_data_format)
        output_valid_data_path = '{}/{}.valid.seg.{}'.format(
            args.output_data_path, args.dataset, args.output_data_format)
        output_test_data_path = '{}/{}.test.seg.{}'.format(
            args.output_data_path, args.dataset, args.output_data_format)

        # write to files
        with open(output_train_data_path, 'w', encoding='utf8') as f:
            for trainl in train_div_data:
                print(trainl, file=f)
            if not args.quiet:
                log('save cooked train data: {}'.format(
                    output_train_data_path))
        with open(output_valid_data_path, 'w', encoding='utf8') as f:
            for validl in valid_div_data:
                print(validl, file=f)
            if not args.quiet:
                log('save cooked validdata: {}'.format(output_valid_data_path))
        with open(output_test_data_path, 'w', encoding='utf8') as f:
            for testl in test_div_data:
                print(testl, file=f)
            if not args.quiet:
                log('save cooked test data: {}'.format(output_test_data_path))

    if not args.quiet:
        report(train_div_data, valid_div_data, test_div_data)


def main():
    args = parse_args()
    cook(args)


if __name__ == '__main__':
    main()
