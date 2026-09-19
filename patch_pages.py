files = ['achievements.html', 'about.html', 'skills.html', 'experience.html']
for fname in files:
    with open(fname, 'rb') as f:
        raw = f.read()
    raw = raw.replace(b'style.css?v=3.0', b'style.css?v=4.1')
    raw = raw.replace(b'<body>\r\n', b'<body class="dark-theme">\r\n')
    raw = raw.replace(b'<body>\n', b'<body class="dark-theme">\n')
    with open(fname, 'wb') as f:
        f.write(raw)

for fname in files:
    content = open(fname, encoding='utf-8').read()
    print(fname, '| CSS:', 'v=4.1' in content, '| dark-theme:', 'dark-theme' in content)
