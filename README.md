# SkyEng

CLI for [skyeng.ru](https://skyeng.ru/)

## Installation

1. ...
1. `cp config_example.toml config.toml`
1. Edit `config.toml`

## Usage

Show your wordsets (lessons):

```bash
python3 -m skyeng wordsets
```

Show unknown words from wordset (you can get wordset ID from previous command):

```bash
python3 -m skyeng words --wordset=123456
```

Show already known words from wordset:

```bash
python3 -m skyeng words --wordset=123456 --known
```

Review words from wordset in interactive mode:

```bash
python3 -m skyeng review --wordset=123456
```

Learn words via context training:

```bash
python3 -m skyeng learn --wordset=123456
```
