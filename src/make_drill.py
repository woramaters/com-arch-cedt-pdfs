"""Generate the topic drill markdown (src/drill/*.md) from src/drill-src/*.txt.

Source format (one file per topic):

    %TITLE Performance (Ch2)
    %CODE P
    %REVIEW
    ...markdown shown before the questions...
    %ENDREVIEW
    %PART ก. แนวคิด
    %MC
    question markdown (one or more lines)
    a) option
    b) option
    c) option
    d) option
    =b
    explanation markdown (until the next % directive)
    %SA
    question markdown
    =short answer
    explanation markdown

Questions are numbered per topic (P1, P2, ...). The answers go on a new page
after the questions of the same topic, so each topic can be drilled on its own.
"""
import glob
import os
import re
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'drill-src')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'drill')
OPTION = re.compile(r'^([a-d])\)\s*(.*)$')


def parse(path):
    topic = {'title': '', 'code': '', 'review': [], 'items': []}
    lines = open(path, encoding='utf-8').read().split('\n')
    i = 0
    part = None
    while i < len(lines):
        line = lines[i]
        if line.startswith('%TITLE'):
            topic['title'] = line[6:].strip()
        elif line.startswith('%CODE'):
            topic['code'] = line[5:].strip()
        elif line.startswith('%REVIEW'):
            i += 1
            while not lines[i].startswith('%ENDREVIEW'):
                topic['review'].append(lines[i])
                i += 1
        elif line.startswith('%PART'):
            part = line[5:].strip()
            topic['items'].append({'kind': 'part', 'text': part})
        elif line.startswith('%MC') or line.startswith('%SA'):
            kind = 'mc' if line.startswith('%MC') else 'sa'
            i += 1
            block = []
            while i < len(lines) and not lines[i].startswith('%'):
                block.append(lines[i])
                i += 1
            topic['items'].append(parse_item(kind, block, path))
            continue
        i += 1
    return topic


def parse_item(kind, block, path):
    eq = next((k for k, l in enumerate(block) if l.startswith('=')), None)
    if eq is None:
        sys.exit(f'{path}: item without "=" answer line: {block[:2]}')
    body, answer, why = block[:eq], block[eq][1:].strip(), block[eq + 1:]
    item = {'kind': kind, 'answer': answer, 'why': '\n'.join(why).strip()}
    if kind == 'mc':
        opts = [OPTION.match(l) for l in body]
        idx = [k for k, m in enumerate(opts) if m]
        if len(idx) != 4 or answer not in 'abcd' or len(answer) != 1:
            sys.exit(f'{path}: bad MC item: {body[:2]}')
        item['question'] = '\n'.join(body[:idx[0]]).strip()
        item['options'] = {opts[k].group(1): opts[k].group(2) for k in idx}
    else:
        item['question'] = '\n'.join(body).strip()
    return item


def render(topic):
    code = topic['code']
    out = [f"# {topic['title']}", '', '## สรุปก่อนทำโจทย์', '']
    out += topic['review'] + ['']
    questions = [it for it in topic['items'] if it['kind'] != 'part']
    out += [f'## โจทย์ ({len(questions)} ข้อ)', '']
    n = 0
    for it in topic['items']:
        if it['kind'] == 'part':
            out += [f"### {it['text']}", '']
            continue
        n += 1
        it['no'] = f'{code}{n}'
        if it['kind'] == 'mc':
            out += [':::: q', f"**{it['no']}.** {it['question']}", '', '::: choices']
            for letter in 'abcd':
                out += [f"{letter}) {it['options'][letter]}", '']
            out += [':::', '::::', '']
        else:
            out += ['::: q', f"**{it['no']}.** {it['question']}", '',
                    '<div class="answer-line"></div>', ':::', '']

    out += ['```{=html}', '<div class="pagebreak"></div>', '```', '',
            f"## เฉลย: {topic['title']}", '']
    mcs = [it for it in questions if it['kind'] == 'mc']
    for k in range(0, len(mcs), 10):
        chunk = mcs[k:k + 10]
        out.append('| ข้อ | ' + ' | '.join(it['no'] for it in chunk) + ' |')
        out.append('|---|' + '---|' * len(chunk))
        out.append('| ตอบ | ' + ' | '.join(it['answer'] for it in chunk) + ' |')
        out.append('')
    for it in questions:
        if it['kind'] == 'mc':
            head = f"**{it['no']}. ตอบ [{it['answer']}) {it['options'][it['answer']]}]{{.ans}}**"
        else:
            head = f"**{it['no']}. [{it['answer']}]{{.ans}}**"
        out += ['::: sol', head, '']
        if it['why']:
            out += [it['why'], '']
        out += [':::', '']
    return '\n'.join(out) + '\n'


def main():
    os.makedirs(OUT, exist_ok=True)
    for old in glob.glob(os.path.join(OUT, '*.md')):
        os.remove(old)
    # Hand-written pages (e.g. the intro) are copied through unchanged.
    for page in glob.glob(os.path.join(SRC, '*.md')):
        text = open(page, encoding='utf-8').read()
        open(os.path.join(OUT, os.path.basename(page)), 'w', encoding='utf-8').write(text)
    total = 0
    for path in sorted(glob.glob(os.path.join(SRC, '*.txt'))):
        topic = parse(path)
        name = os.path.splitext(os.path.basename(path))[0] + '.md'
        open(os.path.join(OUT, name), 'w', encoding='utf-8').write(render(topic))
        count = sum(1 for it in topic['items'] if it['kind'] != 'part')
        total += count
        print(f'{name}: {count} questions')
    print(f'total: {total} questions')


if __name__ == '__main__':
    main()
